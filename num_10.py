print (" ")
print (" Piedra Gonzalez Rodrigo 3-w # de control 1204")
print (" ")

# Creamos una lista llamada 'frutas' que contiene los nombres de varias frutas
frutas = ["naranja", "uvas", "Melon", "Durazno", "Toronja", "cereza", "Tomate"]

# Inicializamos una variable 'i' con el valor 0, que será utilizada como índice para acceder a los elementos de la lista
i = 0

# Usamos un bucle 'while' para iterar a través de la lista de frutas
# El bucle continuará ejecutándose mientras 'i' sea menor que la longitud de la lista (len(frutas))
while i < len(frutas):
    # Imprimimos el elemento en la posición 'i' de la lista 'frutas'
    print(frutas[i])
    
    # Incrementamos 'i' en 1 para mover al siguiente elemento de la lista en la siguiente iteración
    i += 1
