print( "Programme exo 14 annee bissextile")

annee = int(input ("entrer une annee : "))

if (annee%4 ==0 and annee%100!=0 or annee%400 ==0):
    print("l'annee est bissextile")

else:
    print ("l'annee n'est pas bissextile")
