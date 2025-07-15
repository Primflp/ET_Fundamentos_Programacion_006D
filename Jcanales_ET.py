productos = {

 #productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video]

 "8475HD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i5", "Nvidia GTX1050"],
 "2175HD": ["lenovo", 14, "4GB", "SSD", "512GB", "Intel Core i5", "Nvidia GTX1050"],
 "JjfFHD": ["Asus", 14, "16GB", "SSD", "256GB", "Intel Core i7", "Nvidia RTX2080Ti"],
 "fgdxFHD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i3", "integrada"],
 "GF75HD": ["Asus", 15.6, "8GB", "DD", "1T", "Intel Core i7", "Nvidia GTX1050"],
 "123FHD": ["lenovo", 14, "6GB", "DD", "1T", "AMD Ryzen 5", "integrada"],
 "342FHD": ["lenovo", 15.6, "8GB", "DD", "1T", "AMD Ryzen 7", "Nvidia GTX1050"],
 "UWU131HD": ["Dell", 15.6, "8GB", "DD", "1T", "AMD Ryzen 3", "Nvidia GTX1050"],
 }  

stock = {

 #stock = {modelo: [precio, stock], ...]


 "8475HD": [387990,10],
 "2175HD": [327990,4], 
 "JjfFHD": [424990,1],
 "fgdxFHD": [664990,21], 
 "123FHD": [290890,32], 
 "342FHD": [444990,7],
 "GF75HD": [749990,2], 
 "UWU131HD": [349990,1], 
 "FS1230HD": [249990,0], 

 }

"""
*** MENU PRINCIPAL ***
1. Stock marca.
2. Búsqueda por precio.
3. Actualizar precio.
4. Salir.
"""



"""La opción 1 (Stock marca) debe entregar el stock de una marca particular ingresada por
teclado. La marca ingresa puede estar escrita en mayúscula o minúsculas y debe funcionar
de igual manera. Debe estar implementada mediante una función llamada
stock_marca(marca) que recibe como parámetro la marca y no debe retornar nada."""


def stock_marca(marca):

    for modelosP, datosP in productos.items():
        if datosP[0] == marca:

            for modelosS, datosS in stock.items():
                if modelosP == modelosS:
                    print(f"Modelo: {modelosS}, precio: {datosS[0]}, quedan {datosS[1]} unidades.")
    return True

def busqueda_precio(p_min, p_max):

    print("Los productos disponibles a ese precio son:")
    for modelo, datos in stock.items():
        if datos[0]>=p_min and datos[0]<=p_max and datos[1]>0:
            print(f"Modelo: {modelo}, precio: {datos[0]}, quedan {datos[1]} unidades.")

def actualizar_precio(modelo, p):

    for modelos_stock, datos in stock.items():
        if modelos_stock==modelo:
            datos[0]=p
            print(f"Modelo: {modelo}, precio: {datos[0]}")
            return True
    return False
        
while True:
    try:
    
        print("""
*** Bienvenido a Pybooks ***
    1. Stock marca.
    2. Búsqueda por precio.
    3. Actualizar precio.
    4. Salir.""")

        opcion=int(input("Ingrese una opcion: "))

        match opcion:

            case 1:
                marca=input("\nIngrese la marca que desea ver el stock: ")

                for modelo, nombre in productos.items():
                    nombre[0]=nombre[0].lower()

                if stock_marca(marca.lower()):

                    print("\nLa marca que esta buscando no existe.")

                else:
                    
                    print(" ")
                    

            case 2:

                p_min=int(input("Ingrese el precio minimo para buscar: "))
                p_max=int(input("Ingrese el precio minimo para buscar: "))

                busqueda_precio(p_min, p_max)

            case 3:
                while True:
                    modelo=input("Que modelo desea actualizar: ")
                    p=int(input("Ingrese el nuevo precio del modelo: "))

                    if actualizar_precio(modelo, p):
                        print("Precio actualizado!!.")

                    else:
                        print("El modelo no existe!!")

                    otro=input("Desea actualizar otro precio?: ")

                    if otro.lower()=="si":
                        print(" ")
                    elif otro.lower()=="no":
                        break
                    else:
                        print("Escoja entre si y no.")

            case 4:
                print("Saliendo del menu... ")
                print("Programa finalizado.")
                break
            case _:
                print("Debe seleccionar una opción válida!!")

    except Exception as e:
            print("Error: ",e)




    
    
    