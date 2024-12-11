def cycle(iterable):
    items = list(iterable)
    while True:
        yield from items

def take(generator, n):
    return [next(generator) for _ in range(n)]

def chain(*iterables):
    for iterable in iterables:
        yield from iterable

if __name__ == "__main__":
    result = take(cycle([1, 2, 3]), 10)
    print(result)  

    my_list = [42, 13, 7]
    result = list(chain([1, 2, 3], ['a', 'b'], my_list))
    print(result)

    result = take(cycle(chain([1, 2, 3], ["A", "c"], ("Z", "f"))), 10)
    print(result)
