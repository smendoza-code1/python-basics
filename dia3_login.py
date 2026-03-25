usuario = input("ingresa tu usuario: ") 
contraseña = input("ingresa tu contraseña: ")

if usuario == "admin" and contraseña == "1234":
    print("acceso concedido")
else:
    print("acceso denegado")