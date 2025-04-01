# type something
# find location of characters from start to last without using rindex() function
# print output

# type something
phrase = input("enter a string: ")
target = input("enter the substring to find: ")

# find location of characters from start to last without using rindex() function
position = -1  
for i in range(len(phrase) - len(target), -1, -1):  # Loop backward
    if phrase[i:i + len(target)] == target:
        position = i
        break  

# print output
if position != -1:
    print(f"'{target}' first appears at index {position} (starting from the end).")
else:
    print(f"The substring '{target}' was not found in the string.")
