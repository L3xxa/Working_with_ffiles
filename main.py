search = input('Enter the word you want to search: ')
overwritten = input('Enter the word you want to replace: ')

with open('origin.txt', 'r') as file:
    text = file.read()

updated_text = text.replace(search, overwritten)

print(updated_text)

with open('overwrite.txt', 'w') as file:
    file.write(updated_text)