# [2, 1, 5, 1, 3, 2], k=3
def max_sub_array_of_size_k(k, arr):
    max_sum = 0
    window_start = 0

    for i in range(len(arr)-k+1):
        window_sum = 0
        for window_end in range(i,i+k):
            window_sum += arr[window_end]
        
        max_sum = max(window_sum, max_sum)
    
    return max_sum

