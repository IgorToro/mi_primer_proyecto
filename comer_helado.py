apetece_helado_input = input("¿Te apetece un helado? (Si / No):").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("Te he dicho que digas Si o No, no se que me has dicho, cuento como que no quieres un helado")
    apetece_helado = False

tienes_dinero_input = input("¿Tienes dinero? (Si / No):").upper()

if tienes_dinero_input == "SI":
    tienes_dinero = True
elif tienes_dinero_input == "NO":
    tienes_dinero = False
else:
    print("Te he dicho que digas Si o No, no se que me has dicho, cuento como que no tienes dinero")
    tienes_dinero = False

senor_helados_input = input("¿Esta el heladero? (Si / No):").upper()

if senor_helados_input == "SI":
    senor_helados = True
elif senor_helados_input == "NO":
    senor_helados = False
else:
    print("Te he dicho que digas Si o No, no se que me has dicho, cuento como que no esta el heladero")
    senor_helados = False

tu_tia_input = input("¿Esta tu tia? (Si / No):").upper()

if tu_tia_input == "SI":
    tu_tia = True
elif tu_tia_input == "NO":
    tu_tia = False
else:
    print("Te he dicho que digas Si o No, no se que me has dicho, cuento como que no esta tu tia")
    tu_tia = False

apetece_helado = apetece_helado_input == "SI"
tienes_dinero = tienes_dinero_input == "SI"
senor_helados = senor_helados_input == "SI"
tu_tia = tu_tia_input == "SI"
puede_permitirselo = tienes_dinero or tu_tia

if apetece_helado and puede_permitirselo and senor_helados:
    print("Pues comete un helado")
else:
    print("Pues nada")
