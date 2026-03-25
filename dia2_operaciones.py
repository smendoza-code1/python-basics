nombre = input("Como te llamas? ")
peso = input("Cuanto pesas? ")
altura = input("Cuanto mides en metros? ")

peso = float(peso)
altura = float(altura)

imc = peso/altura**2 

print(f"Hola {nombre}")
print(f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    print("bajo peso")
elif imc < 25:
    print("peso normal")
elif imc < 39:
    print("sobrepeso")
else:
    print("obesidad")