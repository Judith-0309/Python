from math import *

n = int(input("entrer la valeur de n :"))
S = 0
for i in range(1, n-1):
        r = n % i

while r == 0:
    S = S + i
if S == n:
    print("n est parfait")
else:
    print("n n'est pas parfait")

