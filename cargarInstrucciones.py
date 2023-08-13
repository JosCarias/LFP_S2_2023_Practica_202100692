#Clase para cargar cambios en el inventario
#se ejecuta al escoger la opcione 2 del menu
def getCargarInstrucciones():

    #importacion de clases a las cuales se les hace mencion mas adelanta
    from cargarInventario import imprimirInventario, leerArchivosInv
    from menuPrincipal import getMenuPrincipal

    #variable temporal en la cual se van a guardar los procesos
    inventario ={}

    #bienvendia del fomulario
    print("---------------------------------------------------")
    print("Cargar Instrucciones")
    print("---------------------------------------------------")

    #captura de direciones relativas de los archivos .inv y . mov
    print("Ingrese la direccion relativa del archivo inventario")
    rutaInventario=input()
    print("Ingrese la direccion relativa del archivo movimiento")
    rutaMovimiento=input()

    #llamado a las clases que hacen los procesos
    inventario=leerArchivosInv(rutaInventario)
    inventario=cargarCambios(rutaMovimiento,inventario)
    imprimirInventario(inventario)
    actualizarInventario(rutaInventario, inventario)

    #salida le programa
    print("---------------------------------------------------")
    print("Presiciones cualquier tecla para continuar")
    input()
    getMenuPrincipal()

#Clase para dentificar los movimientos del inventario y sus respectivas acciones
#recibe 2 atribitos la ruta del archivo .mov y el invetario cargado del archivo .inv
def cargarCambios(rutaMovimiento, ubicaciones):
    #intendo te procesar el archivo .mov
    try:
        with open(rutaMovimiento, encoding="utf-8") as file:
            #leer el archivo en lineas
            for linea in file:
                instruccion, informacion = linea.strip().split(" ")
                producto, cantidad, ubicacion = informacion.split(";")
                #proceso de agregar
                if instruccion == "agregar_stock":
                    if ubicacion not in ubicaciones:
                        print("Esa ubicacion no existe")
                        continue
                    if producto not in ubicaciones[ubicacion]:
                        print("Ese producto no existe en esa ubicacion")
                        continue
                    ubicaciones[ubicacion][producto]['cantidad'] += float(cantidad)   
                #procesos de vender
                elif instruccion == "vender_producto":
                    if ubicacion not in ubicaciones:
                        print("Esa ubicacion no existe")
                    if ubicacion not in ubicaciones or producto not in ubicaciones[ubicacion]:
                        print("Ese producto no esta en esa ubicacion") 
                    cantidadVender = float(cantidad)
                    cantidadDisponible = ubicaciones[ubicacion][producto]['cantidad']
                    if cantidadVender > cantidadDisponible:
                        print("Error: La cantidad de producto no está disponible",producto, cantidad, ubicacion,informacion)
                    else:
                        ubicaciones[ubicacion][producto]['cantidad'] -= float(cantidadVender)
        return ubicaciones
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
        getCargarInstrucciones()
    except IOError:
        print("Error al leer el archivo.")
        getCargarInstrucciones()
#clase para reescribir el inverio con los cambio se agregar y ventas
def actualizarInventario(rutaInventario, inventario):
    #intento de reescritura
    try:
        with open(rutaInventario, "w") as archivo_inv:
            for ubicacion, ubicaciones in inventario.items():
                for producto, detalles in ubicaciones.items():
                    cantidad = detalles["cantidad"]
                    precio = detalles["precio"]
                    archivo_inv.write(f"crear_producto {producto};{cantidad};{precio};{ubicacion}\n")
        print("Archivo de inventario actualizado correctamente.")
    except IOError:
        print("Error al escribir en el archivo de inventario.")
        getCargarInstrucciones()