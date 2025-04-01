# type something
# add zeroes without using zfill() function
# print output 

# type something
phrase = input("enter a string or number: ")
width = int(input("enter the total width: "))

# add zeroes without using zfill() function
if len(phrase) < width:
    zeros = width - len(phrase)
    phrase = '0' * zeros + phrase

# print output
print(phrase)
