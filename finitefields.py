import math
primes = [2]
for num in range(3,62,2):
    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
       primes.append(num)

for p in primes:
    for i in range(p):
        print ([1 if i * j % p == 1 else 0 for j in range(p)])