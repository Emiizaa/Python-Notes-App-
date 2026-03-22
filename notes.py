import json #aqui importamos la funcion json
import os #aqui la funcion operating system
nombre_archivo = "notas.json" #aqui le indicamos a python que nombre_archivo significa notas.json para asi ahorrarnos recordar el nombre del archivo en un futuro


def guardar_cambios(notas): #bueno aqui definimos este funcion para pues como su nombre dice, a continuacion te digo lo que significa, notA: solo le pone algo entre parentisis si es que el codigo necesita algo externo para funcionar, o sea, algo que no este dentro de la funcion, en caso de quer no, no pongas parentesis
    with open(nombre_archivo, "w") as archivo: #aqui basicamente le dices a python que, abra el archivo "notas.json"(el cual definimos como nombre_archivo hasta arriba del codigo), y que, en caso de que no alla, cree uno (w signifca write el crea uno nuevo) y lo apodamos temporalmente "archivo"
        json.dump(notas, archivo) #aqui basicamente le decimos a python que, todo lo que este en notas lo pase al archivo (notas.json) todo esto con el json.dump, entre parentisis pues de donde sacvar los daots (notas) y a donde pasarlos (archivo)
def cargar_notas():
    """Lee el archivo JSON. Si no existe, devuelve una lista vacía.""" 
    if os.path.exists(nombre_archivo):#aqui basicamente le dices que, si existe el archivo
        with open(nombre_archivo, "r") as archivo:·#aqui pues le dices que lo abra y que lo lea "r" significa read y lo apodamos com archivo
            return json.load(archivo) #aqui basicamente le dices que, devuela el contenido de el archivo "traducido" para poder ser tomando en cuenta en el codigo, el que "traudce" es json.load, el parentesis es lo que lo traduce, y el return pues le dice que nos lo devuelva
    return [] #en caaso de que esto no se cumpla, deja la lista vacia
notas = []
notas = cargar_notas()
def mostrar_notas(notas): #aqui denifnimos pues una funcion para evitar repetir el codigo de mostrar lista
    print("--- TUS NOTAS ---")
    if len(notas) == 0: #linea 19 - 20, aqui basicamente le dices a python que, si la la longitud (len) de lista 0 (longitud es algo asi como elementos) pues imprime "no hay notas"
        print ("no hay notas 🥲, crea una!")
    else: #linea 21 - 23, basicamente primero con i hacemos que tenga numero, con  n hacemos que n equivalga a un cubiculo de notas, cual hacer el print por ejemplo {n['texto']} porque le estas diciendo a pytrhon que texto lo extraiga de n o sea de notas
        for i, n in enumerate(notas):
            print(f"{i + 1}. {n['texto']}, ⭐️" if n["importante"] else f"{i + 1}. {n['texto']}")


while True: #aqui iniciamos un ciclo infinito con while para asi que el usuario no tenga que arrncar el programa cada vez
    print("bienvenido a notas!")
    print("1. Ver notas")
    print("2. Crear una nota")
    print("3. Editar nota")
    print("4. eliminar una nota")
    print("5. Salir")

    opcion = input("ingresa la opción que quieras(número): ") #linea 34 -aqui le preguntamos al usuario que opcion quiere con numero

    if opcion == "1": #aqui le decimos python que si lo que escrbio el usuario es igual a 1, muestre la funcion de mostrar_notas(notas)
        mostrar_notas(notas)

    elif opcion == "2": #lo mismo, comparar resdpuesta de usuario, luego le pregunta al usuario que quiere escribir con el input definiendo que texto es igual a lo que escriba el usuario
        print("crea una nota")
        texto = input("Escribe tu nota: ")
        respuesta = input("¿Es importante? (si/no): ").lower().strip()#aqui de nuevo se le pregunta al usuario si la nota es importante o no, el .lower() y el .strip() sirve para hacer que la respuesta sea en automatico minusculas y se quiten todos los epsacios
        
        importante = False #linea 44 - 50 basicament compara la respuesta del usuario, si es igual a si, entocnes importante es true y la nota es imortante, y si es no entonces importante es false y por lo tanto la nota no es importante
        if respuesta == "si":
            importante = True
        elif respuesta == "no":
            importante = False 
        else:
            print("respuesta inválida")

        nota = { #aqui hacemos un diccionario, texto de este codigo es texto, e importante de esta seccion es importante y que ambos pertencewn a nota
            "texto": texto,
            "importante": importante
        }

        notas.append(nota) #aqui basicamente le decimos a `python que nota lo guarde en la lista notas
        
        guardar_cambios(notas) #ejecutamos la funcion de guardar cambios para que lo guarde en el archivo
    

    elif opcion == "3": #lo mismo, si la resp. del usuario es igual a 3 se mostraran las nitas guardadas
        print("editar nota")
        print("ver las notas")
        mostrar_notas(notas)
        
        nota_a_modificar = int(input("que nota deseas modificar?(numero): ")) #aqui se le pregunta a usuario que escriba el indice de la nota que quiere modficar

        if 1 <= nota_a_modificar <= len(notas): #si respuesta del ususario (la cual es "nota_a_modifcar" y se le resta uno pq antes le sumamos 1 pero python inicia en 0) es mayor o igual a 1 y mas aparte, es menor o igual a la cantidad de elementos que hay en la lista entonces
            nota = notas[nota_a_modificar - 1]

            print("1. Editar texto")
            print("2. Editar importancia")
            print("3. Editar ambos aspectos")

            Modificacion = input("que quieres modificar?(numero): ") #aqui se le pregunta al usuario que diga el indice de nota que quiere modficar

        if Modificacion == "1":
            nuevo_texto = input("ingresa el nuevo texto de la nota: ")
            nota["texto"] = nuevo_texto #aqui se le dice a python que el apartado "texto" de nota es igual a nuevo_texto el cual es lo que escribio el usuario
            print("cambio exitoso")
            guardar_cambios(notas)
    

        elif Modificacion == "2":
            nueva_respuesta = input("es esta nota importante?(si/no): ").lower().strip() #aqui igualmente se le pregunta al usuario si es que la nota que selecciono es importante o no
            if nueva_respuesta == "si": #linea 87 - 96, basicamente si la respuesta del usuario es si, entonces el apartado de nota "importante" de la nota que seleccionaste ahora es true, y si escribiste no, entonces ahora es false, si escribe otra cosa se le marcara como respuesta invalida
                nota["importante"] = True
                print("cambio exitoso!")
                guardar_cambios(notas)
            elif nueva_respuesta == "no":
                nota["importante"] = False
                print("cambio exitoso!")
                guardar_cambios(notas)
            else:
                print("respuesta no válida")
                        

        elif Modificacion == "3":
            nuevo_texto = input("ingresa el nuevo texto de la nota: ") #linea 100 - 114, aqui basicamente repetimos lo mismo que en la modficacion 1 y 2, practicamente solo copiamos y pegamos el codigo todo junto 
            nota["texto"] = nuevo_texto
            print("texto editado con éxito!")
            guardar_cambios(notas)
            nueva_respuesta = input("es esta nota importante?(si/no): ").lower().strip()
            if nueva_respuesta == "si":
                nota["importante"] = True
                print("cambio exitoso!")
                guardar_cambios(notas)
            elif nueva_respuesta == "no":
                nota["importante"] = False
                print("cambio exitoso!")
                guardar_cambios(notas)
            else:
                print("respuesta no válida")



    elif opcion == "4": 
        mostrar_notas(notas) #mostramos las notas guardadas mediante la funcion mostrar notas

        nota_eliminar = int(input("que nota quieres eliminar?(numero): ")) #en esta parte solamente se le pregunta al usuario con int e input (necesitamos numero para restarle 1 y que python sepa que elemento de la lista nos referimos) cual es el indice de la nota que quiere eliminar

        if 1 <= nota_eliminar <= len(notas): #linea 123 - 128, se compara la respuesta del usuario para verficar si es mayor o igual que uno, y, que sea menor o igual que los elementos totales guardados en la lista 
            notas.pop(nota_eliminar - 1)
            print("nota eliminada")
            guardar_cambios(notas)
        else:
            print("nota inválida")
            
    elif opcion == "5":#aqui solamente hacemos que se rompa el ciclo while true
        print("adiooos, vuelve pronto")
        break


