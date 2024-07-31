responde_a_estimulos = input("¿Responde a estímulos?: ").lower() == "si"

if responde_a_estimulos:
    print("Valorar la necesidad de llevar al hospital más cercano")
else:
    print("Abrir la vía aérea")
    respira = input("¿Respira?: ").lower() == "si"
    if respira:
        print("Permitir posición de suficiente ventilación")
    else:
        print("Administrar 5 ventilaciones y llamar a una ambulancia")

        while True:
            signos_vitales = input("¿Hay signos vitales?: ").lower() == "si"
            if signos_vitales:
                print("Reevaluar a la espera de la ambulancia")
                llego_ambulancia = input("¿Llegó la ambulancia?: ").lower() == "si"
                if llego_ambulancia:
                    print("Se lleva al paciente")
                    break  # salir del bucle si llegó la ambulancia
            else:
                print("Administrar compresiones torácicas hasta que llegue la ambulancia")