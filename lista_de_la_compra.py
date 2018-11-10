mi_lista = []

item_lista = input("¿Que necesitas comprar? (escribe FIN para salir de la lista): ")

while item_lista != "FIN":
    mi_lista.append(item_lista)
    item_lista = input("¿Que necesitas comprar? (escribe FIN para salir de la lista): ")

for producto in mi_lista:
    print("Tengo que comprar {}".format(producto))

print("La lista de la compra ha terminado")
