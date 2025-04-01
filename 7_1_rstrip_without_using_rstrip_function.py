# type something
# remove characters you want like rstrip function but not using rstrip
# print output

# type something
phrase = input("enter a string: ")

# ask user for characters to remove
chars_to_remove = input("enter characters to remove from the end: ")

# remove chosen characters from the end of the string
i = len(phrase) - 1
while i >= 0 and phrase[i] in chars_to_remove:
    i -= 1
new_phrase = phrase[:i + 1]

# Print output
print(new_phrase)
