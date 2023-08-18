nombreUsuario = input("Digita tu nombre: ")
edadUsurio = int(input("Digita tu edad: "))

if  edadUsurio >= 0 and edadUsurio <= 15: 
    print(f"Querido {nombreUsuario}, usted es un niño.")
elif edadUsurio > 15 and edadUsurio <= 28:
    print(f"Querido {nombreUsuario}, usted es un joven.")
elif edadUsurio > 28 and edadUsurio <= 60:
    print(f"Querido {nombreUsuario}, usted es un Adulto.")
elif edadUsurio > 60 and edadUsurio < 110:
    print(f"Querido {nombreUsuario}, usted es un sugar.")
else:
    print(f"Edad no validad")