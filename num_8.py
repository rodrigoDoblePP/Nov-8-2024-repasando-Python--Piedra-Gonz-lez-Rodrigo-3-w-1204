print (" ")
print (" Piedra Gonzalez Rodrigo 3-w # de control 1204")
print (" ")

# Inicializamos la variable 'numero' con el valor 9, que es el número con el que vamos a hacer la multiplicación
numero = 9

# Inicializamos 'resultado' en 0, que se usará para almacenar el resultado de cada multiplicación
resultado = 0

# Iniciamos un bucle 'for' para recorrer los números del 1 al 10 (inclusive)
# 'range(1, 11, 1)' genera una secuencia de números del 1 al 10 (sin incluir el 11), con un paso de 1
for i in range(1, 11, 1):
    # En cada iteración, multiplicamos el 'numero' (9) por el valor de 'i' (el número actual del bucle)
    resultado = numero * i
    
    # Imprimimos el resultado de la multiplicación en el formato "numero * i = resultado"
    print(numero, "*", i, "=", resultado)

# Imprimimos un espacio en blanco, para separar la salida de este bloque con lo que venga después
print(" ")

