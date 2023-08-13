def getCargarInstrucciones():
    from cargarInventario import imprimirInventario, leerArchivosInv
    from menuPrincipal import getMenuPrincipal
    inventario ={}

    print("---------------------------------------------------")
    print("Cargar Instrucciones")
    print("---------------------------------------------------")

    print("Ingrese la direccion relativa del archivo inventario")
    rutaInventario=input()
    print("Ingrese la direccion relativa del archivo movimiento")
    rutaMovimiento=input()

    inventario=leerArchivosInv(rutaInventario)
    inventario=cargarCambios(rutaMovimiento,inventario)
    imprimirInventario(inventario)
    actualizarInventario(rutaInventario, inventario)


    print("---------------------------------------------------")
    print("Presiciones cualquier tecla para continuar")
    input()
    getMenuPrincipal()

def cargarCambios(rutaMovimiento, ubicaciones):
    try:
        with open(rutaMovimiento, encoding="utf-8") as file:
            for linea in file:
                instruccion, informacion = linea.strip().split(" ")
                producto, cantidad, ubicacion = informacion.split(";")
                if instruccion == "agregar_stock":
                    if ubicacion not in ubicaciones:
                        print("Esa ubicacion no existe")
                        continue
                    if producto not in ubicaciones[ubicacion]:
                        print("Ese producto no existe en esa ubicacion")
                        continue
                    ubicaciones[ubicacion][producto]['cantidad'] += float(cantidad)   
                elif instruccion == "vender_producto":
                    if ubicacion not in ubicaciones:
                        print("Esa ubicacion no existe")
                    if ubicacion not in ubicaciones or producto not in ubicaciones[ubicacion]:
                        print("Ese producto no esta en esa ubicacion") 
                    cantidadVender = float(cantidad)
                    cantidadDisponible = ubicaciones[ubicacion][producto]['cantidad']
                    if cantidadVender > cantidadDisponible:
                        print("Error: La cantidad de producto no está disponible")
                    else:
                        ubicaciones[ubicacion][producto]['cantidad'] -= float(cantidadVender)
        return ubicaciones
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
        getCargarInstrucciones()
    except IOError:
        print("Error al leer el archivo.")
        getCargarInstrucciones()

def actualizarInventario(rutaInventario, inventario):
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