from collections import deque
def reverse_string(input_str):
    stack = deque()
    reversed = []
    for ele in input_str:
        stack.append(ele)
    
    for _ in range(len(input_str)):
        reversed += stack.pop()
    
    return ''.join(reversed)

def main():
    print("Reverse: " + str(reverse_string("akash")))

main()

# read the string filename
from collections import OrderedDict
filename = input()
# print(filename)
with open(filename) as fp:
    fp = fp.read()
# print(fp)

res = {}
for line in fp.split("\n"):
    # print(line)
    # print(line.strip().split(' ')[0])
    host = line.strip().split(' ')[0]
    if len(host)==0:
        continue
    
    if res.get(host) is None:
        res[host] = 1
    else:
        res[host] += 1

# print(res)
filename = "records_"+filename
# print(filename)
fp = open(filename, "w")
sor = res.keys()
sor = sorted(sor)
# print(sor)
for k in sor:
    fp.write(k+" "+str(res[k]))
    # fp.write(k)
    # fp.write(res[k])
    print(k, res[k])
fp.close()

# return filename