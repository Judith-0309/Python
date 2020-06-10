a = int(input("entrer la valeur de a : "))
b = int(input("entrer la valeur de b : "))
quotient = 0
while (a >= b):
    a = a - b
    quotient += 1
print("le quotient de la division par soustractions successives est :", quotient)