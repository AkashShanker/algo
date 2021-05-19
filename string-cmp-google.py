'''
def compare_string(str1,str2):
    str1_l = str1.lower()
    str2_l = str2.lower()

    if str1_l == str2_l:
        return True
    else:
        return False
'''
#Considering that the strings are super long, 
# and mostly they are unequal.
'''
def compare_string(str1, str2):
    if len(str1) == len(str2):
        str1_iter = iter(str1)
        str2_iter = iter(str2)

        for _ in range(len(str1)):
            str1_c = next(str1_iter)
            str2_c = next(str2_iter)

            if str1_c.upper() == str2_c.upper():
                return True
            else:
                return False


    else:
        return False
'''
def compare_string(str1, str2, acceptable_val):
    mismatch = 0
    diff_val = len(str1)-len(str2)
#    print(diff_val)
    if len(str1) != len(str2) and diff_val > acceptable_val:
        return -1
    else:
        for i in range(len(str1)):
            if str1[i].lower() != str2[i].lower():
                print(str1[i].lower(),str2[i].lower())
                mismatch += 1
                if mismatch > acceptable_val:
                    return -2
                else:
                    if i == len(str1)-1:
                        return True
                    else:
                        continue
            else:
                continue

    # else:
    #     return True

def main():
    str1 = "Akash"
    str2 = "akSH"
    print(compare_string(str1,str2, 1))

main()