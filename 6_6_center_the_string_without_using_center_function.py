# type something   
# center without using center()
# print output

# type something   
string = input("enter a string: ")
width = int(input("enter the desired width: "))

# center without using center()
total_padding = width - len(string)

# split padding evenly
if total_padding > 0:
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding
    string = (' ' * left_padding) + string + (' ' * right_padding)

# print output
print(f"'{string}'")