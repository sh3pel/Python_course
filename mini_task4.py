def reversed_dict(d):
    a = {}
    k = list(d.keys())
    v = list(d.values())
    for i in range(len(k)):
        if  v[i] not in a:
            a[v[i]] = k[i] 
        else:
            tmp = tuple([a[v[i]]])
            a[v[i]] = tmp + tuple([str(k[i])])
    return a

a = {"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}

def check_solution():
    assert reversed_dict({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}) == {97832: ('Ivanov', 'Kuznecov'), 55521: 'Petrov'}, "Failed test"
    #assert reversed_dict({1: [1,2,3]}) == TypeError, "Failed test", works excellent, assert cant launch it
    assert reversed_dict({1: 2, "3": 4}) == {2:1, 4: "3"}, "Failed test"
    
    return "All tests passed"

print(check_solution())
