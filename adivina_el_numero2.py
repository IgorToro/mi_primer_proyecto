numero_a_adivinar = int(input("Teclea el numero a adivinar: "))
numero_del_usuario = int(input("Adivina el numero: "))

while numero_a_adivinar != numero_del_usuario:
    print("¡Has fallado!")
    numero_del_usuario = int(input("Vuelve a intentarlo: : "))

print("¡Has acertado!")
