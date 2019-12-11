# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrrayA, arrayB ):
    elements = len( arrrayA ) + len( arrayB )
    merged_arr = [0] * elements
    a = 0
    b = 0
    # TO-DO
    for i in range(elements):
        if a == len(arrrayA):
            merged_arr[i] = arrayB[b]
            b += 1
        elif b == len(arrayB):
            merged_arr[i] = arrrayA[a]
            a += 1
        elif arrrayA[a] < arrayB[b]:
            merged_arr[i] = arrrayA[a]
            a += 1
        else:
            merged_arr[i] = arrayB[b]
            b += 1
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( array ):
    # TO-DO
    n = len(array)
    mid = n // 2
    if n > 1:
        left = merge_sort(array[0: mid])
        right = merge_sort(array[mid:])
        array = merge(left, right)

    return array


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr