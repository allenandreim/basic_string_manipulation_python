# type something
# startswith without usin startswith() function
# print output 

# Type something
phrase = input("Enter a string: ")
prefix = input("enter the prefix to check: ")

# startswith without usin startswith() function
starts_with_prefix = phrase[:len(prefix)] == prefix

# print output
print(starts_with_prefix)
