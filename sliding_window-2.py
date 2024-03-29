#Input: [2, 1, 5, 2, 3, 2], S=5
#Output: 2
#Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
import math

def smallest_subarray_with_given_sum(s,arr):
    window_start = 0
    window_sum = 0
    min_len = math.inf

    for window_end in range(0, len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            min_len = min(min_len,window_end - window_start + 1) #3
            window_sum -= arr[window_start]
            window_start += 1
    if min_len == math.inf:
        return 0
    return min_len

def main():
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))
main()