from itertools import count

with open('text.txt', 'r') as file:
    content = file.read()

read = content.split()
count_words = 0

for i in read:
    count_words += 1

print(count_words)


