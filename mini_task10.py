def singleton(cls):
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
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
