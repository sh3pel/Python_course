def deprecated(since=None, will_be_removed=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            name = func.__name__
            if since and will_be_removed:
                print(f"Warning: function {name} is deprecated since version {since}. It will be removed in version {will_be_removed}.")
            elif since:
                print(f"Warning: function {name} is deprecated since version {since}. It will be removed in future versions.")
            elif will_be_removed:
                print(f"Warning: function {name} is deprecated. It will be removed in version {will_be_removed}.")
            else:
                print(f"Warning: function {name} is deprecated. It will be removed in future versions.")

            return func(*args, **kwargs)
        return wrapper
    return decorator 

@deprecated()
def foo():
    print("Hello from foo")

@deprecated(since="4.2.0", will_be_removed="5.0.1")
def bar():
    print("Hello from bar")

foo()
bar()