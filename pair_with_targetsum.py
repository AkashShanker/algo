
#Brute Force
def pair_with_targetsum(arr, target_sum):
  sum = 0
  for ln in range(len(arr)):
    for k in range(len(arr)):
      sum = arr[ln] + arr [ln+k]
      
      if sum == target_sum:
        return [ln, ln+k]
