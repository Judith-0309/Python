from math import *


a = int(input("donner le 1er nombre : "))
b = int(input("donner le 2eme nombre : "))

r = int(b % a)
PGCD = int(a - r)
PPCM = int(a*b / PGCD)
print("le plus grand commun diviseur est: ", PGCD)
print("le plus petit commun diviseur est: ", PPCM)

