import re

def find_number(string):
    result = re.findall(r'[-+]?\d*\.\d+|\d+', string)    
    return result

def main():
    string = "My address is 704 S Claremont Avenue and my salary this week is 1013.24 and the temperature is -33.4"
    print(find_number(string))

main()