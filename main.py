with open('text.txt', 'r') as file:
    content = file.read()

count = 0
for i in content:
    count += 1

print(count)

