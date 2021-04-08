def merge_lists(lst1, lst2):
#[1,5,7,8,10] [2,3,4,6,9] - The case only considers unique sorted list
    ind1 = 0
    ind2 = 0
    while (ind1 < len(lst1)) and (ind2 < len(lst2)):
        if(lst1[ind1] > lst2[ind2]):
            lst1.insert(ind1, lst2(ind2))
            ind1+=1
            ind2+=1
        else:
            ind1+=1
    return lst1

def easy_way_out(lst1,lst2)
    new = []
    new = sorted(lst1 + lst2)
    return new