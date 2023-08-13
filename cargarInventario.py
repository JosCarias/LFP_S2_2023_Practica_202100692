#libreria para dar formato a los diccionarios
import json
#clase que se ejecuta en la opcion 1 del menu
def getCargarInicial():
    from menuPrincipal import getMenuPrincipal
    #bienvendida del formulario
    print("---------------------------------------------------")
    print("Inventario Principal")
    print("---------------------------------------------------")
    #captura de ruta de archivo .inv
    print("Ingrese la direccion relativa del archivo")
    ruta=input()
    imprimirInventario(leerArchivosInv(ruta))
    #salida del programa
    print("---------------------------------------------------")
    print("Presiciones cualquier tecla para continuar")
    input()
    getMenuPrincipal()

#clase para leer el archivo .inv y almacenarlo en un diccionario
def leerArchivosInv(ruta):
    ubicaciones ={}
    try:
        with open(ruta, encoding="utf-8") as file:
            for linea in file:
                producto, cantidad, precio, ubicacion= linea.strip().split(" ")[1].split(";")
                if ubicacion in ubicaciones:
                    ubicaciones[ubicacion][producto]={
                        "cantidad": float(cantidad),
                        "precio": float(precio)
                    }
                else:
                    ubicaciones[ubicacion]={
                        producto:{
                            "cantidad": float(cantidad),
                            "precio": float(precio)
                        }
                    }
        return ubicaciones
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
        getCargarInicial()
    except IOError:
        print("Error al leer el archivo.")
        getCargarInicial()

#clase para escribir el inventario en un formato un poco mas leible         
def imprimirInventario(inventario):
    print("---------------------------------------------------")
    print(json.dumps(inventario, indent=4))



