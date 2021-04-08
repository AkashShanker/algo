def find_minimum(arr):
    #arr = [9,2,3,6]
    minval = arr[0]

    for ele in arr[1:]:
        if ele < minval:
            minval = ele
    return minval