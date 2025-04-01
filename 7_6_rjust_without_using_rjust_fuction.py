# type something
# rjust without using rjust() function
# print output 

# type something
phrase = input("enter a string: ")
width = int(input("enter the total width: "))

# rjust without using rjust() function
if len(phrase) < width:
    spaces = width - len(phrase)
    phrase = ' ' * spaces + phrase

# print output
print(phrase)