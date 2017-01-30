from sieve import sieve


def isPandigital(num):
    s = set()
    l = str(num)
    n = len(l)

    for i in l:
        c = int(i)
        if c == 0 or c > n:
            return False

        s.add(i)

    return "0" not in s and len(s) == len(l)

sieveArray = sieve(10**7)
reversedEnumeratedSieveArray = reversed(list(enumerate(sieveArray)))

for (prime, isPrime) in reversedEnumeratedSieveArray:
    if not isPrime:
        continue

    if isPandigital(prime):
        print prime
        break

