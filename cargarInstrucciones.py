from cargarInventario import leerArchivosInv
def getCargarInstrucciones():
    print("---------------------------------------------------")
    print("Instrucciones de movimientos")
    print("---------------------------------------------------")
    print("Ingrese la direccion relativa del archivo")
    ruta_mov=input()
    print("Ingrese la direccion relativa del archivo")
    ruta_invetario=input()
    try:
        with open(ruta_mov, "r") as archivo:
            for linea in archivo:
                instruccion, detalles = linea.strip().split(' ', 1)
                if instruccion == 'agregar_stock':
                    nombre, cantidad, ubicacion = detalles.split(';')
                    cantidad = int(cantidad)
                    agregar(leerArchivosInv(ruta_invetario), nombre, cantidad, ubicacion)
    except FileNotFoundError:
        print(f"El archivo {ruta_mov} no fue encontrado.")
        getCargarInstrucciones()
    except ValueError:
        print("Error: El formato del archivo es incorrecto.")
        getCargarInstrucciones()

def agregar(inventario, nombre, cantidad, ubicacion):
    if nombre in inventario and ubicacion in inventario[nombre]:
        inventario[nombre][ubicacion]['cantidad'] += cantidad
    else:
        print(f"Error: El producto '{nombre}' no existe en la ubicación '{ubicacion}'.")

