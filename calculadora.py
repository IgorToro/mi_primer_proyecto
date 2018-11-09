operacion_elegida = input("¿Que operacion quieres realizar? (Multiplicar / Dividir / Sumar / Restar): ").upper()

primer_numero = int(input("Elije el primer numero: "))
segundo_numero = int(input ("Elije el segundo numero: "))

if operacion_elegida == "MULTIPLICAR":
    resultado = primer_numero * segundo_numero
    print("El resultado de {} los numeros es: {}".format(operacion_elegida, resultado))

if operacion_elegida == "DIVIDIR":
    resultado = primer_numero / segundo_numero
    print("El resultado de {} los numeros es: {}".format(operacion_elegida, resultado))

if operacion_elegida == "SUMAR":
    resultado = primer_numero + segundo_numero
    print("El resultado de {} los numeros es: {}".format(operacion_elegida, resultado))

if operacion_elegida == "RESTAR":
    resultado = primer_numero - segundo_numero
    print("El resultado de {} los numeros es: {}".format(operacion_elegida, resultado))

print("Hemos terminado")
