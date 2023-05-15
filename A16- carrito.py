#
carrito = []
esta_comprando = True

while esta_comprando :
    valor_i =(input("Ingresa valor del producto =="))
    if valor_i == 'salir' :
        esta_comprando = False
    else :
        carrito.append(valor_i)

print (" \n")
valor_total = sum(carrito)
iva = (valor_total / 100) * 19
print("el valor total de su compra es ==> ",valor_total)
print (" \n")
print(f"Sus impuestos fueron del 19% y fueron ==> {iva}")

        