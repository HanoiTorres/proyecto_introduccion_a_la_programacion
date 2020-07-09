
import Menu
import Datos
import Archivo

juega = True
opcion = 0
prestamo = []

while(juega == True):
    Menu.imprimirMenu()
    persona =  Archivo.readPersonas()
    libro = Archivo.readLibros()
    print("Indique la opcion: ")
    opcion = int (input())

    if (opcion == 8):
       juega = False
       print("")
       print("ADIOS")
    if (opcion == 1):
      print("Opcion 1")

      #print(listPersonas)
      print(persona)

    if (opcion == 2):
         print("Opcion 2")

         for k in sorted(persona): print(k, persona[k])

         print(persona)


    if (opcion == 3):

        print("La lista tiene un total de  los siguientes indices : =>", Datos.lenPersona(persona), " Empezando en 0 Digite el indice que desea ver ")
        indice = int (input())

        print(persona[indice])

    if (opcion == 4):

          print(libro)


    if (opcion == 5):

         print("Que quiere buscar")
         texto = str (input())

         i = 0
         while (i < len(libro)):
             if(libro[i]["nombre"].find(texto) >= 0):

                 print(libro[i])
                 break
             i = i + 1


    if (opcion == 6):
        print(persona)
        print("")
        print("Seleccione el Id de la Persona")
        idPersona = int (input())
        print("")
        print(libro)
        print("")
        print("Seleccione el Id del libro")
        idLibro = int (input())
        nuevoPrestamo = {"IdPersona": idPersona, "IdLibro": idLibro}
        prestamo.append(nuevoPrestamo)

    if (opcion == 7):
        print(prestamo)



# print("")
# input("Presione una tecla para continuar")
