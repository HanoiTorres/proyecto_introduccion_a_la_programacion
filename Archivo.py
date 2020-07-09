
def readPersonas():

    archivo = open("personas.csv", "r")

    lin = 1
    keys = []
    diccionario = {}
    carro = 0

    for linea in archivo.readlines():
        lineaEnArreglo = linea.split(",")
        if(lin == 1):
            keys = lineaEnArreglo
            # print (keys)
        else:
            k = 0
            diccionarioTMP = {}
            while (k < len(keys)):
                diccionarioTMP[keys[k]] = lineaEnArreglo[k]
                k = k + 1
                diccionario[carro] = diccionarioTMP

                carro = carro + 1
        lin = lin + 1
    archivo.close()
    return diccionario

def readLibros():

    archivo = open("libros.csv", "r")

    lin = 1
    keys = []
    diccionario = {}
    carro = 0

    for linea in archivo.readlines():
        lineaEnArreglo = linea.split(",")
        if(lin == 1):
            keys = lineaEnArreglo
            
        else:
            k = 0
            diccionarioTMP = {}
            while (k < len(keys)):
                diccionarioTMP[keys[k]] = lineaEnArreglo[k]
                k = k + 1
                diccionario[carro] = diccionarioTMP

                carro = carro + 1
        lin = lin + 1
    archivo.close()
    return diccionario
