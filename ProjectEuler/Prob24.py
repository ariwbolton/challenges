import math
from itertools import permutations

total = 0

for value in permutations(list(range(10))):
    total += 1

    if total == 1000000:
        print(value)




    

    
        
