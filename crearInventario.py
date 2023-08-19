#clase para saber la fecha
from datetime import date
#clase llamada en la opcion 3 del inventario
def setInventario():
    #importacion de clases llamadas mas adelanta 
    from menuPrincipal import getMenuPrincipal
    from cargarInventario import leerArchivosInv
    #bienvenida del formulario
    print("---------------------------------------------------")
    print("Informe de Inventario")
    print("---------------------------------------------------")
    #captura de direcciones 
    print("Ingrese la ruta relativa del inventario")
    ruta=input()
    inventario=leerArchivosInv(ruta)
    salida(inventario)
    crearInforme(inventario)
    #salida del formulario
    print("---------------------------------------------------")
    print("Presiciones cualquier tecla para continuar")
    input()
    getMenuPrincipal()

#imprecion del informe de invetario
def salida(inventario):
    print("Producto"+"   "+"Cantidad"+"   "+"Precio unitario"+"   "+"Valor total"+"   "+"Ubicacion")
    print("------------------------------------------------------------------")
    for producto, ubicaciones in inventario.items():
        for ubicacion, detalles in ubicaciones.items():
            cantidad = detalles["cantidad"]
            precio = detalles["precio"]
            print(f"{producto} {cantidad} ${precio:.2f} ${cantidad * precio:.2f} {ubicacion}")

#clase para crear el archivo .txt con el informe
def crearInforme(inventario):
    fecha=str(date.today())+".txt"
    try:
        with open(fecha, "w") as archivo:
            archivo.write("Producto Cantidad Precio Unitario Valor Total Ubicacion\n")
            archivo.write("-------------------------------------------------\n")
            for producto, ubicaciones in inventario.items():
                for ubicacion, detalles in ubicaciones.items():
                    cantidad = detalles["cantidad"]
                    precio = detalles["precio"]
                    linea = f"{producto}     {cantidad}     ${precio:.2f}     ${cantidad * precio:.2f}      {ubicacion}\n"
                    archivo.write(linea)
        print("Inventario guardado en el archivo correctamente.")
    except IOError:
        print("Error al escribir informe.")
