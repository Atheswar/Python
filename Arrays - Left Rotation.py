def array_left_rotation(a, n, k):
    k = k % n  
    return a[k:] + a[:k]

if _name_ == "_main_":
    n, d = 5, 4
    a = [1, 2, 3, 4, 5]
    result = array_left_rotation(a, n, d)
    print(result)  
