print (" ")
print (" Piedra Gonzalez Rodrigo 3-w # de control 1204")
print (" ")

# Pido al usuario que ingrese su calificación y la convierto a un número entero
nota = int(input("¿Cual es tu Calificacion? :"))

# Verifico en qué rango se encuentra la calificación y doy la respuesta adecuada
if nota >= 0 and nota < 5:
    print("SUSPENSO")  # Si la calificación es entre 0 y 4, es un suspenso
elif nota >= 5 and nota < 6:
    print("SUFICIENTE")  # Si la calificación está entre 5 y 6, es suficiente
elif nota >= 6 and nota < 7:
    print("BIEN")  # Si la calificación está entre 6 y 7, es un 'Bien'
elif nota >= 7 and nota < 9:
    print("NOTABLE")  # Si la calificación está entre 7 y 8, es un 'Notable'
elif nota >= 9 and nota <= 10:
    print("SOBRESALIENTE")  # Si la calificación está entre 9 y 10, es sobresaliente
else:
    print("NOTA NO VÁLIDA")  # Si la calificación es menor que 0 o mayor que 10, es inválida
