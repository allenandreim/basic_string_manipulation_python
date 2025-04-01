# type something
# removesuffix without using removesuffix() funtion
# print output 

# type something
phrase = input("enter a string: ")
suffix = input("enter the suffix to remove: ")

# removesuffix without using removesuffix() funtion
if phrase.endswith(suffix):
    phrase = phrase[:-len(suffix)]

# print output
print(f"Processed string: '{phrase}'")
