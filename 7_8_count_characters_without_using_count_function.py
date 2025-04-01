# type something
# count specific characters without using count() function
# print output 

# type something
phrase = input("enter a string: ")
character = input("enter the character or substring to count: ")

# count specific characters without using count() function
count = 0
for i in range(len(phrase) - len(character) + 1):
    if phrase[i:i+len(character)] == character:
        count += 1

# print output
print(count)