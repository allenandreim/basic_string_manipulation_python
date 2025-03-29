# type something
# title case without using title() function
# print output 

# type something
phrase = input("enter a string: ")
words = phrase.split()
result = ""

# title case without using title() function
for word in words:
    if len(word) > 0:
        capitalized_word = word[0].upper() + word[1:].lower()
        result += capitalized_word + " "

# print output 
result = result.strip()
print(result)

