print (" ")
print (" Piedra Gonzalez Rodrigo 3-w # de control 1204")
print (" ")


# Primer bucle: Genera una pirámide de parentesis ascendente
# 'range(1, 6)' genera los números del 1 al 5, es decir, 1, 2, 3, 4, 5
for i in range(1, 6):
    # Imprime una cantidad de parentesis "*" igual al valor de 'i' en cada iteración
    print("*" * i)

# Segundo bucle: Genera una pirámide de parenteisis descendente
# 'range(-4, 0)' genera los números -4, -3, -2, -1
# El signo negativo invertido en '*-i' hace que se genere la cantidad correcta de parentesis
for i in range(-4, 0):
    # Imprime una cantidad de parentesis "*" igual al valor absoluto de 'i' (ya que '*-i' convierte a 'i' en positivo)
    print("*" * -i)
