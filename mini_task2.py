def myZip(x, y):
    return [(x[i], y[i]) for i in range(min(len(x), len(y)))]

def check_solution():
    assert myZip([1,2,3], ["a","b"]) == [(1,"a"), (2,"b")], "Failed test"
    assert myZip(["a",2,"b"], [1,3,4,"c"]) == [("a", 1), (2,3), ("b",4)], "Failed test"
    assert myZip([1], []) == [], "Failed test"

    return "All tests passed"

print(check_solution())
