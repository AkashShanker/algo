# Remove even numbers from a given list
def remove_even(lst):
    odd=[]
    if ele % 2 !=0:
        odd.append(ele)
    return odd

'''
Pythonic way - Use list comprehension
'''

def pythonic_remove_even(lst):
    return [odd for ele in lst if ele % 2 != 0]