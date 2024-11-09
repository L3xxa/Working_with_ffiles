with open('origin.txt') as file:
    content = file.read()

with open('overwrite.txt', 'w') as output_file:
    output_file.writelines(content)