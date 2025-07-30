inventario={}
cantidad= int(input("Ingrese la cantidad de productos a ingresar: "))
for i in range(cantidad):
    print(f"\nProducto {i+1}")
    while True:
        codigo = input("Ingrese codigo del producto: ")
        nombre = input("Ingrese nombre del producto: ")
        precio = float(input("Ingrese precio del producto: "))
        stock = int(input("Ingrese cantidad de stock del producto: "))
        talla = input("Ingrese la talla del producto: ").upper()
        if codigo in inventario:
            print("Codigo ya existente")
            continue
        if precio <=0:
            print("Precio invalido")
            continue
        if stock <=0:
            print("Cantidad invalida")
            continue
        if talla not in ["S","M","L","XL"]:
            print("Talla invalida")
            continue
        break
