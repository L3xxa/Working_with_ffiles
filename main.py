with open('origin.txt', 'r') as file:
    lines = file.readlines()

max_line = 0
for line in lines:
        count_char = 0
        for char in line:
            count_char += 1
        if count_char > max_line:
            max_line = count_char
print(f"Maximum string length = {max_line}")