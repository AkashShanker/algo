from heapq import *

def Sorting(lst):
    lenMap = {}
    new_lst = []
    for ele in lst:
        lenMap[ele] = len(ele)
    
    {new_lst.append(k) for k,v in sorted(lenMap.items(), key=lambda item: item[1])}
    return new_lst
        

lst = ["rohan", "amy", "sapna", "muhammad", 
       "aakash", "raunak", "chinmoy"]
print(Sorting(lst))