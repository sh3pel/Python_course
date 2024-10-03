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

def check_solution():
    assert solve(10) == 2, "Failed test"
    assert solve(-123) == 3, "Failed test"
    assert solve(129) == 2, "Failed test"
    assert solve(-7) == 2, "Failed test"
    assert solve(0) == 0, "Failed test"
    assert solve(1024) == 1, "Failed test"
    assert solve(-1024) == 1, "Failed test"
    
    return "All tests passed"

print(check_solution())
