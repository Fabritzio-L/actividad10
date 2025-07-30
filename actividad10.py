inventario={}
cantidad= int(input("Ingrese la cantidad de productos a ingresar: "))
for i in range(cantidad):
    print(f"\nProducto {i+1}")
    while True:
        codigo = input("Ingrese codigo del producto: ")
        if codigo in inventario:
            print("Codigo ya existente. Ingrese otro codigo")
        else:
            break
    nombre = input("Ingrese nombre del producto: ")
    categoria= input("Ingrese categoria del producto: ")
    while True:
        precio = float(input("Ingrese precio del producto: "))
        if precio <=0:
            print("El precio no puede ser negativo ni cero.")
        else:
            break
    while True:
        stock = int(input("Ingrese cantidad de stock del producto: "))
        if stock <=0:
            print("La cantidad del producto no puede ser negativa ni cero")
        else:
            break
    while True:
        talla = input("Ingrese la talla del producto: ").upper()
        if talla not in ["S","M","L","XL"]:
            print("Talla invalida")
        else:
            break
    inventario[codigo]= {
        "Nombre": nombre,
        "Categoria": categoria,
        "Precio": precio,
        "Stock": stock,
        "Talla": talla
    }
