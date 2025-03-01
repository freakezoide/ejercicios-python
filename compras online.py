# Lista de productos disponibles en la tienda online
productos = {
    "1": {"nombre": "Laptop", "precio": 800.0},
    "2": {"nombre": "Smartphone", "precio": 500.0},
    "3": {"nombre": "Audífonos", "precio": 50.0},
    "4": {"nombre": "Mouse", "precio": 25.0},
    "5": {"nombre": "Teclado", "precio": 45.0},
}

carrito = []

def mostrar_menu():
    print("\n🛒 Menú de Compras Online")
    print("1. Ver productos disponibles")
    print("2. Agregar producto al carrito")
    print("3. Ver carrito")
    print("4. Eliminar producto del carrito")
    print("5. Finalizar compra")
    print("6. Salir")

def ver_productos():
    print("\n📦 Productos disponibles:")
    for clave, producto in productos.items():
        print(f"{clave}. {producto['nombre']} - ${producto['precio']:.2f}")

def agregar_al_carrito():
    ver_productos()
    codigo = input("Ingrese el número del producto a agregar: ")
    if codigo in productos:
        carrito.append(productos[codigo])
        print(f"✅ {productos[codigo]['nombre']} agregado al carrito.")
    else:
        print("❌ Producto no encontrado.")

def ver_carrito():
    if not carrito:
        print("\n🛒 Tu carrito está vacío.")
        return
    print("\n🛍️ Productos en el carrito:")
    total = 0
    for i, producto in enumerate(carrito, 1):
        print(f"{i}. {producto['nombre']} - ${producto['precio']:.2f}")
        total += producto["precio"]
    print(f"💰 Total a pagar: ${total:.2f}")

def eliminar_del_carrito():
    ver_carrito()
    if not carrito:
        return
    try:
        indice = int(input("Ingrese el número del producto a eliminar: ")) - 1
        if 0 <= indice < len(carrito):
            eliminado = carrito.pop(indice)
            print(f"❌ {eliminado['nombre']} eliminado del carrito.")
        else:
            print("⚠️ Número inválido.")
    except ValueError:
        print("⚠️ Ingresa un número válido.")

def finalizar_compra():
    ver_carrito()
    if carrito:
        print("\n💳 Procesando pago...")
        print("🎉 ¡Compra realizada con éxito! Te llegará un correo con la confirmación.")
        carrito.clear()

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            ver_productos()
        elif opcion == "2":
            agregar_al_carrito()
        elif opcion == "3":
            ver_carrito()
        elif opcion == "4":
            eliminar_del_carrito()
        elif opcion == "5":
            finalizar_compra()
        elif opcion == "6":
            print("👋 ¡Gracias por comprar con nosotros!")
            break
        else:
            print("⚠️ Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()
