# Input: "Programming"
# Output: "rrggmmPiano"
from heapq import *

def sort_character_by_frequency(string):
    alphaMap = {}
    maxHeap = []

    for ele in string:
        alphaMap[ele] = alphaMap.get(ele,0) + 1
    
    for char, frequency in alphaMap.items():
        heappush(maxHeap,(-frequency, char))
    
    finalString = []
    while maxHeap:
        frequency, char = heappop(maxHeap)
        for _ in range(-frequency):
            finalString.append(char)
    
    return "".join(finalString)

def main():
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()