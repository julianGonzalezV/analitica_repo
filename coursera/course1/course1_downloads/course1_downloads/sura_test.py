import numpy as np
# Respuesta 7-1: Matriz de unos de "x" filas y "y" columnas
def matriz1(x, y):
    return np.ones((x, y))
r71 = matriz1(2,3)
print("Respuesta 7-1 => ",r71)    

# Respuesta 7-2: Dado x filas y Y columnas y una lista l
# entonces retornar una matriz de la forma x,y
def matriz2(x,y,l):
    return np.asarray(l).reshape(x, y)
   
r72 = matriz2(2,3,[1,2,3,4,5,6])
print("Respuesta 7-2=> ", r72)

# Respuesta 7-3 , dado un valor retorne la fila y columna en la que se encuentra en la matriz de entrada
def getLocation(value, matriz):
    return np.where(matriz == value)
r73 = getLocation(4, r72)

print("Respuesta 7-3=> ", r73)

# Respuesta 7-4, función que recibe una matriz y la invierte
def reverseMatriz(matriz):
    narr = []
    for row in matriz:
        narr.append(row[::-1])
    return narr
# tes        
r74 = reverseMatriz([[1,3,5],[2,4,6]])
print("Respuesta 7-4=> ", r74)



# Respuesta 8:
# Funcion que dada un iterable y una función entonces aplica la
# funcion a cada elemento de iterable

iterable = [1,2,3,4,5]

def f(iterInput, functionInput):
    return list(map(functionInput,iterInput))

print("Respuesta 8: ")
for answer in f(iterable, lambda x: x*x):
    print(answer)
