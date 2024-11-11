with open('origin.txt', 'w') as file:
    file.write("This is a sample text with several words.")

with open('origin.txt', 'r') as file:
    content = file.read()

read = content.split()
count_words = 0

for i in read:
    count_words += 1

print(count_words)


