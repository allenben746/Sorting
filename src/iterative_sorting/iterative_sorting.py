 TO-DO: Complete the selection_sort() function below 
def selection_sort( array ):
    # loop through n-1 elements
    for i in range(0, len(array) - 1):
        cur_index = i
        small_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range (i+1, len(array)):
            if array[x]<array[small_index]:
                small_index=x 
        # TO-DO: swap
        array[i], array[small_index]=array[small_index], array[i]
    print("Array sorted ->", array)
    return array

exampleArray = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( array ):
    for i in range(0, len(array)-1):
        for j in range(0, len(array)-1):
            if array[j+1]<array[j]:
                print(f"{array[j+1]}<{array[j+1]}")
                array[j+1], array[j]=array[j], array[j+1]
            else:
                print(f"{array[i+1]}!<{array[i+1]}")
    print("sorted array", array)            
    return array

bubble_sort(exampleArray)

# STRETCH: implement the Count Sort function below
