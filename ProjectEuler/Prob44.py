import heapq
from math import sqrt

n = 10000

def isPentagonal(p):
    n = (1 + int(sqrt(1 + (24 * p)))) // 6

    return ithPentagonal(n) == p

def ithPentagonal(p):
    return (p * ((3*p) - 1)) // 2

class Pair:
    # x1 < x2
    def __init__(self, x1, x2):
        self.x1, self.x2 = x1, x2
        self.D = self.x2 - self.x1

    def __le__(self, p2):
        return self.D <= p2.D

    def __repr__(self):
        return "D: " + str(self.D) + ", x1: " + str(self.x1) + ", x2: " + str(self.x2)

heap = list()

print("Creating heap")

pentagonals = list()

for i in range(1, n):
    p1, p2 = ithPentagonal(i), ithPentagonal(i+1)

    j = i-1

    while j > 0 and pentagonals[j-1] + p1 >= p2:
        if isPentagonal(pentagonals[j-1] + p1) and isPentagonal(p1 - pentagonals[j-1]):
            heap.append(Pair(pentagonals[j-1], p1))
        j -= 1

    pentagonals.append(p1)

print("Preparing to heapify")

heapq.heapify(heap)
print("Heapified")


while len(heap) != 0:
    smallest = heapq.heappop(heap)

    if isPentagonal(smallest.D):
        print(smallest)
        exit()

print("No numbers found")

