#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>

static void matrix_mult(float **a, float **b, float **result, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            result[i][j] = 0;
            for (int k = 0; k < n; k++) {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }
}

static float **matrix_power(float **matrix, int n, int exp) {
    float **result = (float **)malloc(n * sizeof(float *));
    for (int i = 0; i < n; i++)
        result[i] = (float *)malloc(n * sizeof(float));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j)
                result[i][j] = 1.0;
            else
                result[i][j] = 0.0;
        }
    }

    while (exp) {
        if (exp % 2) {
            float **temp = (float **)malloc(n * sizeof(float *));
            for (int i = 0; i < n; i++)
                temp[i] = (float *)malloc(n * sizeof(float));
            matrix_mult(result, matrix, temp, n);
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    result[i][j] = temp[i][j];
            for (int i = 0; i < n; i++)
                free(temp[i]);
            free(temp);
        }
        float **temp = (float **)malloc(n * sizeof(float *));
        for (int i = 0; i < n; i++)
            temp[i] = (float *)malloc(n * sizeof(float));
        matrix_mult(matrix, matrix, temp, n);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                matrix[i][j] = temp[i][j];
        for (int i = 0; i < n; i++)
            free(temp[i]);
        free(temp);
        exp /= 2;
    }

    return result;
}

static PyObject *foreign_matrix_power(PyObject *self, PyObject *args) {
    PyObject *input_matrix;
    int exp;

    if (!PyArg_ParseTuple(args, "Oi", &input_matrix, &exp)) {
        return NULL;
    }

    Py_ssize_t n = PyList_Size(input_matrix);
    float **matrix = (float **)malloc(n * sizeof(float *));
    
    for (Py_ssize_t i = 0; i < n; i++) {
        PyObject *row = PyList_GetItem(input_matrix, i);
        matrix[i] = (float *)malloc(n * sizeof(float));
        for (Py_ssize_t j = 0; j < n; j++) {
            matrix[i][j] = (float)PyFloat_AsDouble(PyList_GetItem(row, j));
        }
    }

    float **result = matrix_power(matrix, n, exp);

    PyObject *result_list = PyList_New(n);
    for (Py_ssize_t i = 0; i < n; i++) {
        PyObject *row = PyList_New(n);
        for (Py_ssize_t j = 0; j < n; j++) {
            PyList_SetItem(row, j, PyFloat_FromDouble(result[i][j]));
        }
        PyList_SetItem(result_list, i, row);
    }
    for (Py_ssize_t i = 0; i < n; i++) {
        free(matrix[i]);
        free(result[i]);
    }
    free(matrix);
    free(result);

    return result_list;
}

static PyMethodDef ForeignMethods[] = {
    {"foreign_matrix_power", foreign_matrix_power, METH_VARARGS, "Возводит матрицу в степень."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef foreignmodule = {
    PyModuleDef_HEAD_INIT,
    "foreign",
    NULL,
    -1,
    ForeignMethods
};

PyMODINIT_FUNC PyInit_foreign(void) {
    return PyModule_Create(&foreignmodule);
}