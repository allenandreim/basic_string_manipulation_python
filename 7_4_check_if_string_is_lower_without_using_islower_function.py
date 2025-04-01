# type something
# check if string is lower without using islower() function
# print output 

# type something
phrase = input("enter a string: ")
all_lower = True  

# check if string is lower without using islower() function
for char in phrase:
    if 'A' <= char <= 'Z':
        all_lower = False
        break 

# print output
print(all_lower)
