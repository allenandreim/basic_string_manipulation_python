# type something   
# justifiy to left without using ljust()
# print output

# type something   
# take user inputs for the string, width, and fill character
phrase = input("enter a string: ")
width = int(input("enter the desired width: "))
fill_char = input("enter the fill character (default is space): ")

# default space
if not fill_char:
    fill_char = ' '

# calculate desired width
padding = width - len(phrase)


if padding > 0:
    phrase += fill_char * padding

print(f"'{phrase}'")
