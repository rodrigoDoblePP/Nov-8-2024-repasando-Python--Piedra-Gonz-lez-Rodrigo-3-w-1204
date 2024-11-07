print (" ")
print (" Piedra Gonzalez Rodrigo 3-w # de control 1204")
print (" ")



nombre = input("¿Cuál es tu Nombre? :").lower()  #   convierte a minúsculas
apellido = input("¿Cuál es tu Apellido? :").lower()  #  convierte a minúsculas

# Comprobamos si el nombre y apellido coinciden con los valores predefinidos (en minúsculas)
if nombre == "rodrigo":
    if apellido == "piedra":
        print("Nombre y apellido correcto")
    else:
        print("Apellido incorrecto. El apellido debe ser 'Piedra'.")
else:
    print("Usuario desconocido. El nombre debe ser 'Rodrigo'.")

