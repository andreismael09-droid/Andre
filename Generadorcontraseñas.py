import random



# Evalúa la seguridad de una contraseña según su longitud
def evaluar_contrasena():
    contrasena = input("Ingrese la contraseña a evaluar: ")

    if len(contrasena) < 8:
        print("Contraseña debil")

    elif len(contrasena) < 12: 
        print("Contraseña media")

    else:
        print("Contraseña fuerte")



# Permite al usuario ingresar una contraseña manualmente
def crear_contrasena_manual():
    contrasena = input("Ingrese su contraseña: ")
    print("Contraseña guardada:", contrasena)




# Genera una contraseña aleatoria usando letras, números y símbolos
def generar_contrasena():
    
    longitud = int(input("Ingrese la longitud de la contraseña: "))

    while longitud < 8:
        print("La contraseña debe tener minimo 8 caracteres.")
        longitud = int(input("Ingrese la longitud de la contraseña: "))
    
    contrasena = ""

    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%"
    
    for i in range(longitud):
        caracter = random.choice(caracteres)
        contrasena += caracter

    print("Contraseña generada:", contrasena)




def menu():

    while True:
        print("===== GENERADOR DE CONTRASEÑAS =====")
        print("1. Generar contraseña")
        print("2. Crear contraseña manual")
        print("3. Evaluar contraseña")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ")
    
        if opcion == "1":
            generar_contrasena()
        
        elif opcion == "2":
            crear_contrasena_manual()

        elif opcion == "3":
            evaluar_contrasena()

        elif opcion == "4":
            print("Saliendo del sistema. . .")
            break
        
        else:
            print("Seleccione una opcion valida")

menu()


