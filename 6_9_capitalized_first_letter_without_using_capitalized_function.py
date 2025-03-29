# type something
# capitalized without using capitalized() function
# print output 

# type something
phrase = input("enter a string: ")


if len(phrase) > 0:
    result = phrase[0].upper() + phrase[1:].lower()
else:
    result = phrase

# print output
print(result)