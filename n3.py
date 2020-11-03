from collections import Counter
f = open("GP.txt", "r", encoding="utf8").read()
file = f
print("Количество символов с пробелами: " + str(len(file)))
file = file.split()
file = ''.join(file)
print("Количество символов без пробелов: " + str(len(file)))
num_words = 0
words = []
with open("GP.txt", 'r', encoding='utf8') as f:
    for line in f:
        words += line.split()
        word = line.split()
        num_words+= len(word)
print("Количество слов: " + num_words)
amountRW = num_words - len(Counter(words))
print("Количество слов без повторений: " + str(amountRW))
