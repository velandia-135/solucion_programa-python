# Matriz de inventario
inventario = (
    (101, "computadoras",8,10),
    (102, "impresoras",5,10),
    (103, "Cpus",10,10),
    (104, "maus",15,10),
    (105, "audifonos",12,10)
)

# Funcion para calacular cantidad para pedir
def calcular_pedido(stock_actual,stock_minimo):
    if stock_actual < stock_minimo: 
        return stock_minimo - stock_actual
    else:
        return 0 

# Mostrar lista de pedidos
print("lista de pedidos")
print("-----------------")

for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    print("codigo:",codigo)
    print("articulo:",nombre)
    print("cantidad a pedir:",cantidad_pedir)
    print("------------------------------------")
    
