import unittest
def reversed_dict(d):
    a = {}
    k = list(d.keys())
    v = list(d.values())
    for i in range(len(k)):
        if v[i] not in a:
            a[v[i]] = k[i]
        else:
            tmp = tuple([a[v[i]]])
            a[v[i]] = tmp + tuple([k[i]])
    return a

class TestReversedDict(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(reversed_dict({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}),{97832: ('Ivanov', 'Kuznecov'), 55521: 'Petrov'}, "Failed test")
        self.assertEqual(reversed_dict({1: 2, "3": 4}), {2: 1, 4: "3"}, "Failed test")
        self.assertEqual(reversed_dict({1: 2, "3": 4, 5: 2}), {2: (1,5), 4: "3"}, "Failed test")

    def test_type_error(self):
        with self.assertRaises(TypeError):
            reversed_dict({1: [1, 2, 3]})

if __name__ == '__main__':
    unittest.main()
