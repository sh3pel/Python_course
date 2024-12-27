import functools

def deprecated(func=None, since=None, will_be_removed=None):
    if func is None:
        return lambda f: deprecated(f, since, will_be_removed)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        name = func.__name__
        message_prefix = f"Warning: function {name} is deprecated."
        since_message = f" It is deprecated since version {since}." if since else ""
        removal_message = f" It will be removed in version {will_be_removed}." if will_be_removed else " It will be removed in future versions."
        print(message_prefix + since_message + removal_message)
        return func(*args, **kwargs)
    
    return wrapper

@deprecated
def foo():
    print("Hello from foo.")

@deprecated(since="4.2.0", will_be_removed="5.0.1")
def bar(x, y):
    print(f"Hello from bar with arguments: {x} and {y}")

foo()
bar(10, 20)