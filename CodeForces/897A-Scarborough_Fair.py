import sys

inp = [x.rstrip() for x in sys.stdin.readlines()]

n, m = [int(x) for x in inp[0].split()]
s = list(inp[1])

for line in inp[2:]:
    s_line = line.split()
    l, r = int(s_line[0]), int(s_line[1])
    c1, c2 = s_line[2], s_line[3]

    for i in range(l - 1, r):
        if s[i] == c1:
            s[i] = c2

print("".join(s))