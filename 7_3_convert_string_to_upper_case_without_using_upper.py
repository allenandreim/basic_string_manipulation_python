# type something
# make upper case without using upper() function
# print output

# type something
phrase = input("enter a string: ")

# make upper case without using upper() function
uppercase_phrase = ""
for char in phrase:
    if 'a' <= char <= 'z':  
        uppercase_phrase += chr(ord(char) - 32)  
    else:
        uppercase_phrase += char 

# print output
print(uppercase_phrase)
