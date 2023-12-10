
triangleNums = set()

for i in range(1, 50):
    triangleNums.add((i * (i+1)) // 2)


def isTriangleWord(word):
    total = 0

    for c in word:
        total += (ord(c) - 65) + 1

    return total in triangleNums

words = list()

with open("p042_words.txt", "r") as f:
    lines = f.readlines()

    commaWords = lines[0].split(",")

    for word in commaWords:
        words.append(word[1:-1])

numTriangleWords = 0

for word in words:
    if isTriangleWord(word):
        numTriangleWords += 1

print(numTriangleWords)
