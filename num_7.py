print (" ")
print (" Piedra Gonzalez Rodrigo 3-w # de control 1204")
print (" ")


suma = 0 # Inicializamos una variable 'suma' con valor 0 para almacenar la suma de los números pares

# Usamos un bucle 'for' para iterar a través de los números del 2 al 150, en pasos de 2 (es decir, solo números pares)
# 'range(2, 150, 2)' genera una secuencia de números desde 2 hasta 148 (sin incluir 150), con un paso de 2
for i in range(2, 150, 2):
    
    suma += i# Sumamos el valor de 'i' (el número par actual) a la variable 'suma'


print("La suma de todos los números pares del 2 al 150 es:", suma) # Imprimimos el resultado final, que es la suma de todos 
#los números pares entre 2 y 150
