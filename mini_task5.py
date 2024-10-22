import unittest

def specialize(func, *args, **kwargs):
    def sub_spec(*more_args, **more_kwargs): 
        all_args = args + more_args
        all_kwargs = {**kwargs, **more_kwargs} 
        return func(*all_args, **all_kwargs)
    return sub_spec

def custom_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

class TestReversedDict(unittest.TestCase):
    def test_valid_input(self):
        plus_three = specialize(custom_sum, y=1)
        self.assertEqual(plus_three(10, z=5, a = 15), 31, "Failed test")
        
        just_two = specialize(custom_sum, 1, 1)
        self.assertEqual(just_two(), 2, "Failed test")

if __name__ == '__main__':
    unittest.main()
