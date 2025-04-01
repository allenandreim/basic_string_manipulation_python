# type something
# find location of characters without using index() function
# print output 

# type something
phrase = input("enter a string: ")
character = input("enter the substring to find: ")

# find location of characters without using index() function
position = -1  
for i in range(len(phrase) - len(character) + 1):
    if phrase[i:i + len(character)] == character:
        position = i
        break  

# print output
if position != -1:
    print(position)
else:
    print(f"'{character}' was not found in the string.")
