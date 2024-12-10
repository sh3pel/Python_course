import time
import numpy as np

def generate_random_field(size):
    return np.random.choice([0, 1], size=(size, size), p=[0.5, 0.5])

def game_of_life_python(field, iterations):
    field = field.tolist()  #NUMPY -> list
    rows, cols = len(field), len(field[0])
    
    for _ in range(iterations):
        new_field = [[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                alive_neighbors = sum(field[x][y] for x in range(i-1, i+2) for y in range(j-1, j+2)
                if 0 <= x < rows and 0 <= y < cols and (x != i or y != j))
                if field[i][j] == 1 and alive_neighbors in (2, 3):
                    new_field[i][j] = 1
                elif field[i][j] == 0 and alive_neighbors == 3:
                    new_field[i][j] = 1
        field = new_field
    
    return field

def game_of_life_numpy(field, iterations):
    rows, cols = field.shape
    
    for _ in range(iterations):
        new_field = np.zeros((rows, cols), dtype=int)
        for i in range(rows):
            for j in range(cols):
                alive_neighbors = np.sum(field[i-1:i+2, j-1:j+2]) - field[i, j]
                if field[i, j] == 1 and alive_neighbors in (2, 3):
                    new_field[i, j] = 1
                elif field[i, j] == 0 and alive_neighbors == 3:
                    new_field[i, j] = 1
        field = new_field
    
    return field

initial_field = generate_random_field(128)

import matplotlib.pyplot as plt

# Генерируем начальное поле
initial_field = generate_random_field(128)

# Запуск игры с обычным списком
start_time_python = time.time()
final_field_python = game_of_life_python(initial_field, 128)
end_time_python = time.time()
python_time = end_time_python - start_time_python

# Запуск игры с NumPy
start_time_numpy = time.time()
final_field_numpy = game_of_life_numpy(initial_field, 128)
end_time_numpy = time.time()
numpy_time = end_time_numpy - start_time_numpy

# Сообщаем результаты
print(f"Время выполнения с обычным Python массивом: {python_time:.4f} секунд")
print(f"Время выполнения с NumPy массивом: {numpy_time:.4f} секунд")

# Визуализация результатов
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Результат с обычным Python массивом')
plt.imshow(final_field_python, cmap='binary')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Результат с использованием NumPy массива')
plt.imshow(final_field_numpy, cmap='binary')
plt.axis('off')

plt.show()