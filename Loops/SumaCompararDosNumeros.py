A = input("Ingrese un numero: ")
A = int(A)
B = input("Ingrese un numero: ")
B = float(B)
C = A + B

if A == B:
    print("Los numeros A y B son iguales")
else:
    print("Los numeros A y B son distintos")
    print("Different")

print("El tipo de dato del numero A es: ", type(A))
print("El tipo de dato del numero B es: ", type(B))
print("C = ", C)

if type(A) == type(B):
    print("A y B son el mismo tipo de dato")
else:
    print("A y B son datos de distinto tipo")