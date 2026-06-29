# Lista global para almacenar las citas en la memoria del programa
citas = []


def agendar_cita():
    print("\n--- AGENDAR NUEVA CITA ---")

    # Pedir datos al usuario
    cedula = input("Ingrese la cédula del paciente (10 dígitos): ")

    # Validación simple de cédula (longitud de 10 dígitos)
    if len(cedula) != 10 or not cedula.isdigit():
        print(" Error: La cédula debe tener exactamente 10 números.")
        return

    nombre = input("Nombre del paciente: ")
    if nombre == "":
        print(" Error: El nombre no puede estar vacío.")
        return

    especialidad = input("Especialidad médica: ")
    fecha = input("Fecha de la cita (DD/MM/AAAA): ")
    hora = input("Hora de la cita (HH:MM): ")
    medico = input("Nombre del médico: ")

    # Validación de conflicto de horario (mismo médico, fecha y hora)
    for cita in citas:
        if (
            cita["medico"] == medico
            and cita["fecha"] == fecha
            and cita["hora"] == hora
        ):
            print(" Error: El médico ya tiene otra cita a esa misma hora.")
            return

    # Crear el diccionario con los datos recolectados
    nueva_cita = {
        "cedula": cedula,
        "nombre": nombre,
        "especialidad": especialidad,
        "fecha": fecha,
        "hora": hora,
        "medico": medico,
        "estado": "Pendiente",  # Estado inicial por defecto
    }

    # Guardar en la lista
    citas.append(nueva_cita)
    print(" ¡Cita agendada con éxito!")


def ver_citas():
    print("\n--- LISTADO GENERAL DE CITAS ---")

    if len(citas) == 0:
        print("No hay citas registradas en el sistema.")
        return

    # Recorrer la lista para mostrar cada cita ordenada
    for i in range(len(citas)):
        c = citas[i]
        print(
            f"{i+1}. Paciente: {c['nombre']} | Cédula: {c['cedula']} | "
            f"Esp: {c['especialidad']} | Fecha: {c['fecha']} a las {c['hora']} | "
            f"Dr: {c['medico']} | Estado: {c['estado']}"
        )


def buscar_por_cedula():
    print("\n--- BUSCAR PACIENTE ---")
    cedula_buscar = input("Ingrese la cédula del paciente: ")
    encontrado = False

    for cita in citas:
        if cita["cedula"] == cedula_buscar:
            print(
                f"Cita encontrada -> Paciente: {cita['nombre']} | Fecha: {cita['fecha']} {cita['hora']} | Especialidad: {cita['especialidad']}"
            )
            encontrado = True

    if not encontrado:
        print("No se encontraron citas para esa cédula.")


def actualizar_estado():
    print("\n--- ACTUALIZAR ESTADO DE LA CITA ---")
    ver_citas()  # Mostramos las citas para que el usuario elija

    if len(citas) == 0:
        return

    posicion = (
        int(input("\nSeleccione el número de la cita que desea modificar: "))
        - 1
    )

    if posicion >= 0 and posicion < len(citas):
        print("Estados disponibles: 1. Confirmada | 2. Cancelada")
        opcion = input("Seleccione el nuevo estado (1 o 2): ")

        if opcion == "1":
            citas[posicion]["estado"] = "Confirmada"
            print(" Estado actualizado a 'Confirmada'.")
        elif opcion == "2":
            citas[posicion]["estado"] = "Cancelada"
            print("Estado actualizado a 'Cancelada'.")
        else:
            print(" Opción incorrecta.")
    else:
        print(" El número de cita ingresado no existe.")


def eliminar_cita():
    print("\n--- ELIMINAR CITA ---")
    ver_citas()

    if len(citas) == 0:
        return

    posicion = (
        int(input("\nSeleccione el número de la cita que desea eliminar: "))
        - 1
    )

    if posicion >= 0 and posicion < len(citas):
        confirmacion = input(
            f"¿Seguro que quiere eliminar la cita de {citas[posicion]['nombre']}? (s/n): "
        )
        if confirmacion.lower() == "s":
            citas.pop(posicion)  # Borra el elemento de la lista
            print(" Cita eliminada correctamente.")
        else:
            print("Operación cancelada.")
    else:
        print("Número de cita inválido.")


def ver_estadisticas():
    print("\n--- ESTADÍSTICAS DEL SISTEMA ---")
    total = len(citas)
    print(f"Total de citas registradas hasta el momento: {total}")

    # Contadores simples para estados básicos
    confirmadas = 0
    canceladas = 0
    pendientes = 0

    for cita in citas:
        if cita["estado"] == "Confirmada":
            confirmadas += 1
        elif cita["estado"] == "Cancelada":
            canceladas += 1
        else:
            pendientes += 1

    print(f" - Citas Confirmadas: {confirmadas}")
    print(f" - Citas Canceladas: {canceladas}")
    print(f" - Citas Pendientes: {pendientes}")


def menu_principal():
    # Bucle infinito para mantener el menú corriendo hasta que se elija 'Salir'
    while True:
        print("\n=================================")
        print("   SISTEMA DE CITAS MÉDICAS      ")
        print("=================================")
        print("1. Agendar Cita")
        print("2. Ver Historial Completo")
        print("3. Buscar Paciente por Cédula")
        print("4. Actualizar Estado de Cita")
        print("5. Eliminar Cita")
        print("6. Ver Estadísticas")
        print("7. Salir")

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == "1":
            agendar_cita()
        elif opcion == "2":
            ver_citas()
        elif opcion == "3":
            buscar_por_cedula()
        elif opcion == "4":
            actualizar_estado()
        elif opcion == "5":
            eliminar_cita()
        elif opcion == "6":
            ver_estadisticas()
        elif opcion == "7":
            print("\nMuchas gracias por usar nuestro sistema. ¡Hasta pronto!")
            break  # Rompe el bucle while y cierra el programa
        else:
            print(" Opción inválida. Intente de nuevo.")


# Iniciar el programa principal
menu_principal()
