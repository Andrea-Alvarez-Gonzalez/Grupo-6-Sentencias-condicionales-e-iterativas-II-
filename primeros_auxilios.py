# Funcion que solicita ingresar un dato y convierte la respuesta a un valor booleano
responde_a_estimulos = input("¿Responde a estímulos?:").lower() == "si"

# Verifica si la persona responde a estímulos
if responde_a_estimulos:
    # Si la respuesta es true se imprime un mensaje sobre llevarla al hospital
    print("Valorar la necesidad de llevar al hospital más cercano")
else:
    # Si la respuesta el false se imprime un mensaje que indica abrir la vía aérea
    print("Abrir la vía aérea")
    
    # Funcion que solicita ingresar un dato y convierte la respuesta a un valor booleano
    respira = input("¿Respira?:").lower() == "si"
    
    # El usuario evalúa si la persona respira
    if respira:
        # Si la respuesta en true se imprime un mensaje sobre permitir una posición adecuada para la ventilación
        print("Permitir posición de suficiente ventilación")
    else:
        # Si la respuesta es false se imprime un mensaje sobre administrar ventilaciones y llamar a una ambulancia
        print("Administrar 5 ventilaciones y llamar a una ambulancia")

        # Se genera un bucle que se repetirá continuamente (hasta que llegue la ambulancia)
        while True:
            # Funcion que solicita ingresar un dato y convierte la respuesta a un valor booleano
            signos_vitales = input("¿Hay signos vitales?:").lower() == "si"
            
            # El usuario evalúa si la persona tiene signos vitales
            if signos_vitales:
                # Si la respuesta es true se imprime un mensaje sobre reevaluar mientras se espera la ambulancia
                print("Reevaluar a la espera de la ambulancia")

                # Funcion que solicita ingresar un dato y convierte la respuesta a un valor booleano
                llego_ambulancia = input("¿Llegó la ambulancia?: ").lower() == "si"
                
                # El usuario evalúa si la ambulancia ha llegado
                if llego_ambulancia:
                    # Si la respuesta es true se imprime un mensaje sobre llevar al paciente y se rompe el bucle
                    print("Se lleva al paciente")
                    break  # Se rompe el bucle / FIN
            else:
                # Si la respuesta es false se imprime un mensaje sobre administrar compresiones torácicas hasta que llegue la ambulancia
                print("Administrar compresiones torácicas hasta que llegue la ambulancia")