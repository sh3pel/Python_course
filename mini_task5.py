import unittest
def specialize(func, *args, **kwargs):
    def sub_spec(*more_args):
        all_args = args + more_args
        return func(*all_args, **kwargs)
    return sub_spec

def sum(x, y):
    return x + y

class TestReversedDict(unittest.TestCase):
    def test_valid_input(self):
        plus_one = specialize(sum, y=1)
        self.assertEqual(plus_one(10), 11 , "Failed test")
        
        just_two = specialize(sum, 1, 1)
        self.assertEqual(just_two(), 2, "Failed test")

if __name__ == '__main__':
    unittest.main()

