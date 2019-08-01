dict_1 = {
        'a' : 1,
        'b' : 2,
        'c' : 3,
        'd' : 4,
}


dict_2 = {
        'e' : 5,
        'b' : 7,
        'c' : 8,
        'nd': {
            1:2
        }
}



def merge_dicts(a,b):
    for i in b:
        if isinstance(b[i], dict):
            a[i] = merge_dicts(a.get(i, {}), b[i])
        else:
            a[i] = b[i]
    return a

var = merge_dicts(dict_1, dict_2)
print(var)