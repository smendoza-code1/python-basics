nombre = input("Como te llamas? ")
edad = int(input("Que edad tienes? "))
ciudad = input("Donde vives? ")

if edad < 18:
    print(f"{nombre} de {ciudad}, eres menor de edad.")
elif 18 <= edad <= 60:
    print(f"{nombre} de {ciudad}, eres adulto.")
else:
    print(f"{nombre} de {ciudad}, eres adulto mayor.")
    
