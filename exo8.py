print("Voici le programme de l'exercice 8")
print("Résolution  d'une équation du second degré")
import math
a = float(input("entrer la valeur de a : "))
b = float(input("entrer la valeur de b : "))
c = float(input("entrer la valeur de c : "))
delta = (b*b) - (4*a*c)
if delta < 0:
    print("pas de solution reelle")

elif delta > 0:
    X1 = (-b + math.sqrt(delta))/(2*a)
    X2 = (-b - math.sqrt(delta))/(2*a)
    print("les deux racines sont : X1 et X2" %(X1,X2))

elif (delta == 0):
     X3 = -b/(2*a)
     print("une seule solution :" %X3)

