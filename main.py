with open('origin.txt', 'r') as file:
    lines = file.readlines()

last_line = lines[-1]

with open('last_line.txt', 'w') as file:
    file.writelines(lines[:-1])