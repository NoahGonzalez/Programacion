#Crear un sistema para una empresa de informatica
#El menu debe contener:
#1.-Agregar producto
#2.-listar todos los productos
#3.-eliminar producto po ID
#4.-Generar archivo CSV
#5.- Cargar archivo CSV
#6.-Estadisticas
#7.- salir
#el prodcuto tiene: ID,Nombre,Precio
#En la opcion 6 se imprimen los siguientes datos:
#a.-Precio total de todos los productos
#b.-Promedio del precio de los productos

#Puede desarrolar el ejercicio utilizando lista anidad o lista diccionario
#recuerde utilizar la libreria csv
#Debe utilizar al menos 3 funciones

def acumulador (products):
    acumulador=0
    for x in products:
        acumulador=x[2]+acumulador
    return acumulador


import csv 
  
lista=[]

while (True):
    print ("MENU")
    print ("1.- Agregar producto")
    print ("2.- Listar todos los productos")
    print ("3.- Eliminar productos por nombre")
    print ("4.- Generar un archivo CSV")
    print ("5.- Cargar el archivo CSV")
    print ("6.- Estadisticas")
    print ("0.- Salir")
    
    opcion=int(input("Seleccione su opcion\n"))
    
    if opcion==1:
        print ("PRODUCTOS")
        ID= int(input("Ingrese el ID del producto\n"))
        nombre=input("Ingrese el nombre del producto\n")
        precio=int(input("Ingrese el precio del producto\n"))
        
        nuevalista=[ID,nombre,precio]
        lista.append (nuevalista)
        
        print("Producto Agregado correctamente")
    elif opcion==2:
        print("LISTADO DE PRODUCTOS")
        for productos in lista:
            print ("ID:" ,productos[0],"nombre:",productos [1],"precio:",productos[2])
            print ("--------")
    
    elif opcion ==3:
        print ("ELIMINAR PRODUCTO")
        encontrado=False
        ID= int(input("Ingrese el ID del producto que desea eliminar/n"))
        
        for productos in lista:
            if ID==productos[0]:
                print ("DATOS DEL PRODUCTO A ELIMINAR")
                print ("ID:" ,productos[0],"nombre:",productos [1],"precio:",productos[2])
                lista.remove(productos)
                print("Producto eliminado correctamente")
                encontrado=True
                break
        
        if encontrado== False:
            print("El ID del producto no se encuentra en su carrito")
            
    if opcion==4:
        
        with open ('bdd_productos.csv','w',newline='') as bdd_productos:
            
            escribir_csv=csv.writer(bdd_productos)
          
            escribir_csv.writerow(['ID','nombre','precio'])
            escribir_csv.writerows (lista)
            
        print ("Archivo generado correctamente")
            
    elif opcion==5:
        print ("Cargando archivos CSV...") 
        
        with open ('bdd_productos.csv','r',newline= '') as bdd_productos:
            leer_csv=csv.reader(bdd_productos)
            for fila in leer_csv:
                lista.append(fila)
    
    elif opcion ==6:
        print ("ESTADISTICAS")
        
        acum=0
        products=len(lista)
        acum(lista)
        promedio=int(acum/products)
        
        print(f"hay {products} productos en la lista")
        print(f"Precio total {acum}")
        print(f"Promedio {promedio}")                  
           
                    
                        