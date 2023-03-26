# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 
# Sample String : 'thisisniceone'
# Expected Result : 'thne”'
# Sample String : 'ab'
# Expected Result : 'abab'
# Sample String : 'f'
# Expected Result : Empty String 

str = input('Enter the string: ')
string_length = len(str)
if(string_length < 2):
    print('Empty String')
else:
    output = str[0]+str[1]+str[string_length-2]+str[string_length-1]
    print(output)
