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
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock,
        "talla": talla
    }
print("\nProductos registrados:")
for codigo, datos in inventario.items():
    print(f"\nCodigo: {codigo}")
    print(f"Nombre: {datos["nombre"]}")
    print(f"Categoria: {datos["categoria"]}")
    print(f"Precio: {datos["precio"]}")
    print(f"Stock: {datos["stock"]}")
    print(f"Talla: {datos["talla"]}")
print("\nBusqueda de producto")
buscado = input("Ingrese el codigo del producto a buscar: ")
if buscado in inventario:
    print(f"Nombre: {inventario[buscado]["nombre"]}")
    print(f"Categoria: {inventario[buscado]["categoria"]}")
    print(f"Precio: {inventario[buscado]["precio"]}")
    print(f"Stock: {inventario[buscado]["stock"]}")
    print(f"Talla: {inventario[buscado]["talla"]}")
else:
    print("Codigo de producto no encontrado.")
