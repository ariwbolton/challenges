from collections import deque

s = ""

total = 1

save = deque([1, 10, 100, 1000, 10000, 100000, 1000000])
q = deque()

length, i = 1, 1

while length <= 1000000:
    if len(q) == 0:
        n = str(i)
        q.extend(list(n))
        i += 1

    qVal = q.popleft()

    if length == save[0]:
        save.popleft()
        total *= int(qVal)

    length += 1


print total



