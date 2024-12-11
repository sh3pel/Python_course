def singleton(cls):
    instance = None

    def get_instance(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)  
        return instance 

    return get_instance

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count

@singleton
class GlobalCounter(Counter):
    pass

gc1 = GlobalCounter()
gc2 = GlobalCounter()

gc1.increment()
gc1.increment()

assert id(gc1) == id(gc2)
assert gc1.get_count() == 2  
