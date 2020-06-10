R1 = int(input("Tapez la valeur de l'entier  R1  :  "))
R2 = int(input("Tapez la valeur de l'entier  R2  :  "))
R3 = int(input("Tapez la valeur de l'entier  R3  :  "))
Rs = R1+R2+R3
Rp = (R1*R2*R3)/(R1*R2 + R2*R3 + R1*R3)
choice=int(input("veuillez faire votre choix :"))
if choice == 1 : 
      print("la résistance en série est : Rs = ",Rs)
if choice == 2:
      print("la résistance en série est : Rs = ",Rp)
else :
    print("veuillez revoir la saisie")
