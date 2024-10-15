
def float_matrix(a):
    a = a.split("|")
    mas = []
    for i in range(len(a)):
        mas.append(a[i].split())
        mas = [[float(i) for i in j] for j in mas]
    return mas

def check_solution():
    assert float_matrix("1 2 | 3 4") == [[1.0 , 2.0] , [3.0 , 4.0]], "Failed test"
    assert float_matrix("3.14 | 1.0 21.1 | 23") == [[3.14], [1.0, 21.1], [23.0]], "Failed test"
    
    return "All tests passed"

print(check_solution())