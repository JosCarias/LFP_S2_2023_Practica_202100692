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
    inventario={}
    try:
        with open(ruta, "r") as archivo_inv:
            for linea in archivo_inv:
                instruccion, detalles = linea.strip().split(' ', 1)
                nombre, cantidad, precio_unitario, ubicacion = detalles.split(';')
                inventario[nombre] = {
                    'cantidad': float(cantidad),
                    'precio_unitario': float(precio_unitario),
                    'ubicacion': ubicacion
                }
        return inventario
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
        getCargarInicial()
    except IOError:
        print("Error al leer el archivo.")
        getCargarInicial()
          
def imprimirInventario(inventario):
    print("---------------------------------------------------")
    print(json.dumps(inventario, indent=4))



