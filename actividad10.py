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
    while True:
        categoria= input("Ingrese categoria del producto (Hombre/Mujer/Niño): ").lower()
        if categoria not in ["hombre","mujer","niño"]:
            print("Categoria invalida")
        else:
            break
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
while True:
    print("\nMenu de opciones")
    print("1. Ver productos registrados")
    print("2. Buscar producto por codigo")
    print("3. Consultar valor total del inventario")
    print("4. Contar productos por categoria")
    print("5. Salir")
    opcion = input("Ingrese una de las opciones: ")
    match opcion:
        case "1":
            print("\nProductos registrados:")
            for codigo, datos in inventario.items():
                print(f"\nCodigo: {codigo}")
                print(f"Nombre: {datos["nombre"]}")
                print(f"Categoria: {datos["categoria"]}")
                print(f"Precio: {datos["precio"]}")
                print(f"Stock: {datos["stock"]}")
                print(f"Talla: {datos["talla"]}")
        case "2":
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
        case "3":
            total =0
            for producto in inventario.values():
                total += producto["precio"]*producto["stock"]
            print(f"Valor del inventario: Q{total}")
        case "4":
            hombre = 0
            mujer = 0
            niño = 0
            for prod in inventario.values():
                if prod["categoria"] == "hombre":
                    hombre += 1
                elif prod["categoria"] == "mujer":
                    mujer += 1
                elif prod["categoria"] == "niño":
                    niño += 1
            print("\nCantidad de productos por categoría:")
            print(f"Hombre: {hombre} productos")
            print(f"Mujer: {mujer} productos")
            print(f"Niño: {niño} productos")
        case "5":
            print("Saliendo del programa...")
            break
        case _:
            print("Ingrese una opcion valida")