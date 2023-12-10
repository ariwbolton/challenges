from itertools import permutations

divisors = [2,3,5,7,11,13,17]

total = 0

for p in permutations("0123456789", 10):
    if p[0] == "0":
        continue

    isValid = True

    perm = "".join(list(p))

    for i in range(1, 8):
        if int(perm[i:i+3]) % divisors[i-1] != 0:
            isValid = False
            break

    if isValid:
        total += int(perm)

print(total)