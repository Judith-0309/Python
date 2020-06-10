nbre_secret = 20
nombre = int(input("saisir un nombre :"))
while nombre < nbre_secret:
    print("plus petit")
    nombre = int(input("saisir un nombre : "))

    while nombre > nbre_secret:
        print("plus grand")
        nombre = int(input("saisir un nombre :"))

if nombre == nbre_secret:
    print("Bravo vous avez deviné le nombre secret :" , nbre_secret)