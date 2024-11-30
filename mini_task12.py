def coroutine(f):
    def result(*args, **kwargs):
        c = f(*args, **kwargs)
        next(c) 
        return c
    return result

@coroutine
def storage():
    values = set()
    was_there = False

    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)

st = storage()
print(st.send(42))
print(st.send(42))
print(st.send(13))
print(st.send(13))