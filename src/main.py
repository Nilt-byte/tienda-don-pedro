
from pathlib import Path

archivo = Path("datos/productos.txt")
lineas = archivo.read_text(encoding="utf-8").splitlines()

print("=== Inventario Tienda Don Pedro ===")

productos = []

for linea in lineas:
    if " - $" in linea and not linea.startswith("VENTAS"):
        productos.append(linea)

for producto in productos:
    print("-", producto)

total = 0

for producto in productos:
    precio = producto.split("$")[1]
    precio = int(precio.replace(".", "").replace(",", ""))
    total += precio

print("Total de productos:", len(productos))
print(f"Valor del inventario: ${total}")
