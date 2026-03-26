secreto = 7
numero = int(input("adivina el numero: "))

if numero > secreto:
    print("incorrecto, muy alto.")
elif numero < secreto:
    print("incorrecto, muy bajo.")
else:
    print("correcto, eres el adivinador")