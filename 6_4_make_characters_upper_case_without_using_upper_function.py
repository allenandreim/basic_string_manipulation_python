# type something   
# make characters upper without using upper() function
# print output

# type something   
phrase = input("enter a string: ")
result = ""

# convert all lowercase characters to uppercase without using upper() function
for char in phrase:
    if 'a' <= char <= 'z':  
        result += chr(ord(char) - 32)  
    else:
        result += char 

# print the output
print(result)