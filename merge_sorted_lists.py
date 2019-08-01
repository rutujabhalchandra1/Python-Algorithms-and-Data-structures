
def merge_sorted_arrays(arr1, arr2):
    sorted_arr = []
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            item = arr1.pop(0)
            sorted_arr.append(item)
        else:
            item = arr2.pop(0)
            sorted_arr.append(item)
    sorted_arr.extend(arr1 if arr1 else arr2)
    return sorted_arr

print(merge_sorted_arrays([1,3,4,7],[0,2,5,8,10]))