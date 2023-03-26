# 2. Write a Python program to count the number of characters (character frequency) in a string. 
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

str = input('Enter the string\n')
count = {}
for s in str:
    if s in count:
        count[s]+=1
    else:
        count[s]=1

print(count)
