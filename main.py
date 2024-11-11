search = input('Enter the word you want to search: ')

with open('origin.txt', 'r') as file:
    lines = file.read().split()

count = 0
for line in lines:
    if search in line:
        count += 1
print(count)

