def bubble_sort(arr):
    n = len(arr)
    num_comparisons = 0
    for i in range(n):
        for j in range(0, n-i-1):
            num_comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return num_comparisons

if _name_ == "_main_":
    arr = [3, 2, 1]
    print(bubble_sort(arr))  
    print(arr)  
