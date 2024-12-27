import unittest

def flatten(arr, depth=float("inf")):
    result = []
    for item in arr:
        if isinstance(item, list) and depth > 0:
            result.extend(flatten(item, depth - 1))
        else:
            result.append(item)
    return result

class Test(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(flatten([1, 2, [4, 5], [6, [7]], 8], depth=1), [1, 2, 4, 5, 6, [7], 8], "Failed test")
        self.assertEqual(flatten([1, 2, [4, 5], [6, [7]], 8], depth=2), [1, 2, 4, 5, 6, 7, 8], "Failed test")
        self.assertEqual(flatten([1, 2, [4, 5], [6, [7]], 8]), [1, 2, 4, 5, 6, 7, 8], "Failed test")
        self.assertEqual(flatten([1, 2, [4, 5], [6, [7, [8]]]], depth=3), [1, 2, 4, 5, 6, 7, 8], "Failed test")

    def test_edge_cases(self):
        self.assertEqual(flatten([]), [], "Failed test on empty list")
        
        self.assertEqual(flatten([1]), [1], "Failed test on single item list")
        self.assertEqual(flatten([[1]]), [1], "Failed test on single nested list")
        self.assertEqual(flatten([[[]]]), [], "Failed test on deeply nested empty list")
        
        self.assertEqual(flatten([None]), [None], "Failed test on list with None")
        self.assertEqual(flatten([[None]]), [None], "Failed test on list with None in nested structure")

    def test_negative_cases(self):
        try:
            flatten([1, 2, [3, 4]], depth=-1)
        except IndexError: pass

        try:
            flatten([1, 2, [3, 4]], depth="two")
        except TypeError: pass
        try:
            flatten([1, 2, [3, 4]], nonexistent_argument=5)
        except TypeError: pass
if __name__ == '__main__':
    unittest.main()