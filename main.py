# Array of strings
lines = [
    "The Tale of the Little Kitten",
    "Once upon a time, there was a little fluffy kitten named Murczyk.",
    "He was very curious and always dreamed of going on great adventures.",
    "One day, when all the owners were away, Murczyk decided to fulfill his dream and travel beyond the familiar garden.",
    "After stepping out of the gate, he met an old wise crow sitting on a tree branch.",
    "The crow said: Hello, little kitten. Where are you heading?",
    "I want to see the world and find new friends, - replied Murczyk.",
    "The crow smiled and advised him to go to the Great Forest, where many other animals lived.",
    "Murczyk headed there and soon met a cheerful squirrel named Snowflake.",
    "They became friends and set off together in search of adventures.",
    "On their way, they found an enchanted lake where a golden fish lived, granting wishes.",
    "The fish promised to grant one wish for each of them.",
    "Murczyk wished for wings to fly, while Snowflake dreamed of finding a nut tree with lots of tasty nuts.",
    "The fish fulfilled their wishes, and Murczyk and Snowflake flew together to the nut tree.",
    "They had many adventures, explored new places, and made many new friends among other animals.",
    "Eventually, Murczyk decided to return home, but not alone, but with a great team of friends.",
    "They lived happily together, and their adventures continued for many years.",
    "Murczyk always remembered the day he dared to go beyond the familiar garden, and he realized that true adventures begin when you are ready to take a step forward.",
    "And they lived happily ever after!",
    "I hope you enjoyed this translated tale! If you want more stories or need any other help, let me know."
]


file_path = 'overwrite.txt'

with open(file_path, 'w') as file:
    for line in lines:
        file.write(line + '\n')