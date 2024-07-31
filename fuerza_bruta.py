#Librerias
from getpass import getpass
from string import ascii_lowercase

#Definimos la base de los intentos
intento = 0
posicion_contrasena = 0
contrasena_hack = {}
password_list = {}
password_valido = False

while password_valido != True:
    password = getpass("Ingresa tu contraseña:").lower()
    password_valido = True
    for position, elemento in enumerate(password):
        if password[position] not in ascii_lowercase:
            print("Contraseña erronea. Intenta nuevamente")
            password_valido = False


for position, elemento in enumerate(password):
    password_list[position] = password[position]

while contrasena_hack != password_list:
    for position, elemento in enumerate(ascii_lowercase):
        intento = intento + 1
        if elemento == password[posicion_contrasena]:
            contrasena_hack[posicion_contrasena] = elemento
            posicion_contrasena = posicion_contrasena + 1
            break

    
    
print(f"su contraseña es {contrasena_hack} y se encontro en {intento} de intentos")




