'''
def reverse(input):
    n = len(input)-1
    final = []
    for k in range(len(input)-1):
        final[k] = input[n-k]
    
    return "".join(final)
'''
'''
def reverse(x):
    output = ""
    for c in x:
        output = c + output
        print(output)
def main():
    print(reverse("plip"))

main()

'''

# Find missing items in a list
def missing_number(list1,list2):
    list_1Map = {}
    list_2Map = {}

    for num in list1:
        list_1Map[num] = list_1Map.get(num,0) + 1

    for num in list2:
        list_2Map[num] = list_2Map.get(num,0) + 1
    
    return (list_1Map.items() != list_2Map.items())


def main():
    full_list = [4,9,3,2]
    cmp_list = [9,4,3,2]
    print(missing_number(full_list,cmp_list))

main()
