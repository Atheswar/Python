def minimum_distances(arr):
    index_map = {}
    min_distance = float('inf')
    
    for index, value in enumerate(arr):
        if value in index_map:
            min_distance = min(min_distance, index - index_map[value])
        index_map[value] = index
    
    return min_distance if min_distance != float('inf') else -1

if _name_ == "_main_":
    arr = [7, 1, 3, 4, 1, 7]
    print(minimum_distances(arr))
