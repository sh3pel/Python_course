def exposed_bits(n, to_check):
    result = 0
    while (n != 0):
        if (n & 1 == to_check):
            result += 1
        n >>= 1
    return result

def is_positive(n):
    if n >= 0:
        return exposed_bits(n, True)
    else:
        return exposed_bits(~n, False) + 1

def solve(n):
    return is_positive(n)

print("10:",solve(10))
print("-123:",solve(-123))
print("Answer:", solve(int(input("New test: "))))