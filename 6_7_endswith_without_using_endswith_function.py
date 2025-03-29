# type something
# check ending without using endswith() function
# print output 

# type something
string = input("enter the main string: ")
suffix = input("enter the ending to check: ")

# check ending without using endswith() function
if len(suffix) > len(string):
    result = False
else:
    substring = string[-len(suffix):]
    result = substring == suffix

# print output 
print( result)