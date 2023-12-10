import math

stri = str(math.factorial(100))

tot = 0

for letter in stri:
    tot += int(letter)

print(tot)
