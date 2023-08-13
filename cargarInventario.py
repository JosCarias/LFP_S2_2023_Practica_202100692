import json
def getCargarInicial():
    from menuPrincipal import getMenuPrincipal

    print("---------------------------------------------------")
    print("Inventario Principal")
    print("---------------------------------------------------")

    print("Ingrese la direccion relativa del archivo")
    ruta=input()
    imprimirInventario(leerArchivosInv(ruta))
    
    print("---------------------------------------------------")
    print("Presiciones cualquier tecla para continuar")
    input()
    getMenuPrincipal()

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
          
def imprimirInventario(inventario):
    print("---------------------------------------------------")
    print(json.dumps(inventario, indent=4))



