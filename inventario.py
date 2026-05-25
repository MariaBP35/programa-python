# Matriz de inventario
inventario = [
    ["A001", "Teclado", 4, 10],
    ["A002", "Mouse", 15, 10],
    ["A003", "Monitor", 2, 5],
    ["A004", "Memoria USB", 8, 8],
    ["A005", "Impresora", 1, 4]
]

# Función para calcular cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0

    return cantidad


print("===== LISTA DE PEDIDOS =====\n")

for articulo in inventario:

    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(
        stock_actual,
        stock_minimo
    )

    print("Artículo:", nombre)
    print("Cantidad a solicitar:", cantidad_pedir)
    print("--------------------------")