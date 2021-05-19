# Input : to learn programming refer geeksforgeeks
# Output : geeksforgeeks learn programming refer to

def sortedSentence(string):
    sent_list = string.split(" ")
    sent_list.sort()
    
    return " ".join(sent_list)


Sentence = "to learn programming refer geeksforgeeks"
# Print the sortedSentence
print(sortedSentence(Sentence))
  
Sentence = "geeks for geeks"
# Print the sortedSentence
print(sortedSentence(Sentence))