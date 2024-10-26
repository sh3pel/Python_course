import unittest

def flatten(arr, depth = float("inf")):
    result = []
    for item in arr:
        if isinstance(item, list) and depth > 0: result.extend(flatten(item, depth - 1))
        else: result.append(item)
    return result

class Test(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(flatten([1, 2, [4, 5], [6, [7]], 8], depth = 1), [1, 2, 4, 5, 6, [7], 8], "Failed test")
        self.assertEqual(flatten([1, 2, [4, 5], [6, [7]], 8], depth = 2), [1, 2, 4, 5, 6, 7, 8], "Failed test")
        self.assertEqual(flatten([1, 2, [4, 5], [6, [7]], 8]), [1, 2, 4, 5, 6, 7, 8], "Failed test")
        self.assertEqual(flatten([1, 2, [4, 5], [6, [7, [8]]]], depth = 3), [1, 2, 4, 5, 6, 7, 8], "Failed test")

if __name__ == '__main__':
    unittest.main()