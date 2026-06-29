"""
================================================
  SISTEMA DE AGENDA DE CITAS MÉDICAS
  Proyecto Integrador - Primer Semestre
  Ingeniería en Software
================================================
"""

import os
from datetime import datetime

# ─────────────────────────────────────────────
#   DATOS GLOBALES (lista de citas y pacientes)
# ─────────────────────────────────────────────

citas = []          # Almacena todas las citas
id_contador = 1     # Contador para IDs únicos de citas


# ─────────────────────────────────────────────
#   FUNCIONES AUXILIARES
# ─────────────────────────────────────────────

def limpiar_pantalla():
    """Limpia la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_linea():
    """Imprime una línea decorativa."""
    print("=" * 55)


def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter."""
    input("\n  Presione Enter para continuar...")


def validar_fecha(fecha_str):
    """
    Valida que la fecha tenga el formato DD/MM/AAAA.
    Retorna True si es válida, False si no.
    """
    try:
        datetime.strptime(fecha_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def validar_hora(hora_str):
    """
    Valida que la hora tenga el formato HH:MM (24h).
    Retorna True si es válida, False si no.
    """
    try:
        datetime.strptime(hora_str, "%H:%M")
        return True
    except ValueError:
        return False


def validar_cedula(cedula):
    """
    Valida que la cédula tenga exactamente 10 dígitos numéricos.
    """
    return cedula.isdigit() and len(cedula) == 10


def buscar_cita_por_id(id_buscar):
    """
    Busca una cita por su ID.
    Retorna el índice en la lista, o -1 si no se encontró.
    """
    for i in range(len(citas)):
        if citas[i]["id"] == id_buscar:
            return i
    return -1


def mostrar_cita(cita):
    """Imprime los datos de una cita de forma ordenada."""
    print(f"\n  ID Cita      : {cita['id']}")
    print(f"  Paciente     : {cita['nombre']}")
    print(f"  Cédula       : {cita['cedula']}")
    print(f"  Doctor       : {cita['doctor']}")
    print(f"  Especialidad : {cita['especialidad']}")
    print(f"  Fecha        : {cita['fecha']}")
    print(f"  Hora         : {cita['hora']}")
    print(f"  Motivo       : {cita['motivo']}")
    print(f"  Estado       : {cita['estado']}")


# ─────────────────────────────────────────────
#   MÓDULO 1 — AGENDAR CITA
# ─────────────────────────────────────────────

def agendar_cita():
    """Permite registrar una nueva cita médica."""
    global id_contador

    limpiar_pantalla()
    mostrar_linea()
    print("       AGENDAR NUEVA CITA MÉDICA")
    mostrar_linea()

    # ── Nombre del paciente ──
    nombre = input("\n  Nombre completo del paciente: ").strip()
    if nombre == "":
        print("\n  ⚠  El nombre no puede estar vacío.")
        pausar()
        return

    # ── Cédula ──
    cedula = input("  Cédula (10 dígitos)        : ").strip()
    if not validar_cedula(cedula):
        print("\n  ⚠  La cédula debe tener exactamente 10 dígitos numéricos.")
        pausar()
        return

    # ── Especialidad ──
    print("\n  Especialidades disponibles:")
    print("    1. Medicina General")
    print("    2. Pediatría")
    print("    3. Ginecología")
    print("    4. Cardiología")
    print("    5. Traumatología")

    opcion_esp = input("\n  Seleccione especialidad (1-5): ").strip()
    especialidades = {
        "1": ("Medicina General", "Dr. Carlos Pérez"),
        "2": ("Pediatría",        "Dra. Ana Gómez"),
        "3": ("Ginecología",      "Dra. María Torres"),
        "4": ("Cardiología",      "Dr. Luis Medina"),
        "5": ("Traumatología",    "Dr. Jorge Ruiz")
    }

    if opcion_esp not in especialidades:
        print("\n  ⚠  Opción inválida.")
        pausar()
        return

    especialidad, doctor = especialidades[opcion_esp]

    # ── Fecha ──
    fecha = input("  Fecha de la cita (DD/MM/AAAA): ").strip()
    if not validar_fecha(fecha):
        print("\n  ⚠  Formato de fecha incorrecto. Use DD/MM/AAAA.")
        pausar()
        return

    # ── Hora ──
    hora = input("  Hora de la cita (HH:MM, 24h) : ").strip()
    if not validar_hora(hora):
        print("\n  ⚠  Formato de hora incorrecto. Use HH:MM (ej: 09:30).")
        pausar()
        return

    # ── Verificar que no haya conflicto de horario con el mismo doctor ──
    for c in citas:
        if c["doctor"] == doctor and c["fecha"] == fecha and c["hora"] == hora and c["estado"] != "Cancelada":
            print(f"\n  ⚠  El {doctor} ya tiene una cita el {fecha} a las {hora}.")
            pausar()
            return

    # ── Motivo ──
    motivo = input("  Motivo de la consulta       : ").strip()
    if motivo == "":
        motivo = "No especificado"

    # ── Guardar cita ──
    nueva_cita = {
        "id":           id_contador,
        "nombre":       nombre,
        "cedula":       cedula,
        "doctor":       doctor,
        "especialidad": especialidad,
        "fecha":        fecha,
        "hora":         hora,
        "motivo":       motivo,
        "estado":       "Pendiente"
    }

    citas.append(nueva_cita)
    id_contador += 1

    print(f"\n  ✔  Cita registrada con éxito. ID de cita: {nueva_cita['id']}")
    pausar()


# ─────────────────────────────────────────────
#   MÓDULO 2 — VER TODAS LAS CITAS
# ─────────────────────────────────────────────

def ver_citas():
    """Muestra todas las citas registradas."""
    limpiar_pantalla()
    mostrar_linea()
    print("          LISTADO DE CITAS MÉDICAS")
    mostrar_linea()

    if len(citas) == 0:
        print("\n  No hay citas registradas aún.")
        pausar()
        return

    for cita in citas:
        mostrar_cita(cita)
        print("  " + "-" * 45)

    pausar()


# ─────────────────────────────────────────────
#   MÓDULO 3 — BUSCAR CITA POR CÉDULA
# ─────────────────────────────────────────────

def buscar_por_cedula():
    """Busca todas las citas de un paciente por su cédula."""
    limpiar_pantalla()
    mostrar_linea()
    print("         BUSCAR CITAS POR CÉDULA")
    mostrar_linea()

    cedula = input("\n  Ingrese la cédula del paciente: ").strip()

    encontradas = []
    for cita in citas:
        if cita["cedula"] == cedula:
            encontradas.append(cita)

    if len(encontradas) == 0:
        print(f"\n  ⚠  No se encontraron citas para la cédula: {cedula}")
    else:
        print(f"\n  Se encontraron {len(encontradas)} cita(s):\n")
        for cita in encontradas:
            mostrar_cita(cita)
            print("  " + "-" * 45)

    pausar()


# ─────────────────────────────────────────────
#   MÓDULO 4 — ACTUALIZAR ESTADO DE CITA
# ─────────────────────────────────────────────

def actualizar_estado():
    """Permite cambiar el estado de una cita (Pendiente/Confirmada/Cancelada)."""
    limpiar_pantalla()
    mostrar_linea()
    print("        ACTUALIZAR ESTADO DE CITA")
    mostrar_linea()

    try:
        id_cita = int(input("\n  Ingrese el ID de la cita: ").strip())
    except ValueError:
        print("\n  ⚠  El ID debe ser un número.")
        pausar()
        return

    indice = buscar_cita_por_id(id_cita)

    if indice == -1:
        print(f"\n  ⚠  No se encontró ninguna cita con ID {id_cita}.")
        pausar()
        return

    print(f"\n  Cita encontrada:")
    mostrar_cita(citas[indice])

    print("\n  Nuevo estado:")
    print("    1. Pendiente")
    print("    2. Confirmada")
    print("    3. Cancelada")

    opcion = input("\n  Seleccione (1-3): ").strip()
    estados = {"1": "Pendiente", "2": "Confirmada", "3": "Cancelada"}

    if opcion not in estados:
        print("\n  ⚠  Opción inválida.")
        pausar()
        return

    citas[indice]["estado"] = estados[opcion]
    print(f"\n  ✔  Estado actualizado a: {estados[opcion]}")
    pausar()


# ─────────────────────────────────────────────
#   MÓDULO 5 — ELIMINAR CITA
# ─────────────────────────────────────────────

def eliminar_cita():
    """Elimina una cita del sistema por su ID."""
    limpiar_pantalla()
    mostrar_linea()
    print("            ELIMINAR CITA")
    mostrar_linea()

    try:
        id_cita = int(input("\n  Ingrese el ID de la cita a eliminar: ").strip())
    except ValueError:
        print("\n  ⚠  El ID debe ser un número.")
        pausar()
        return

    indice = buscar_cita_por_id(id_cita)

    if indice == -1:
        print(f"\n  ⚠  No se encontró ninguna cita con ID {id_cita}.")
        pausar()
        return

    print(f"\n  Cita a eliminar:")
    mostrar_cita(citas[indice])

    confirmacion = input("\n  ¿Está seguro de eliminar esta cita? (s/n): ").strip().lower()

    if confirmacion == "s":
        citas.pop(indice)
        print("\n  ✔  Cita eliminada correctamente.")
    else:
        print("\n  ✘  Operación cancelada.")

    pausar()


# ─────────────────────────────────────────────
#   MÓDULO 6 — RESUMEN ESTADÍSTICO
# ─────────────────────────────────────────────

def ver_resumen():
    """Muestra un resumen estadístico de las citas."""
    limpiar_pantalla()
    mostrar_linea()
    print("         RESUMEN DEL SISTEMA")
    mostrar_linea()

    total = len(citas)
    pendientes  = 0
    confirmadas = 0
    canceladas  = 0

    conteo_esp = {}

    for cita in citas:
        # Contar por estado
        if cita["estado"] == "Pendiente":
            pendientes += 1
        elif cita["estado"] == "Confirmada":
            confirmadas += 1
        elif cita["estado"] == "Cancelada":
            canceladas += 1

        # Contar por especialidad
        esp = cita["especialidad"]
        if esp in conteo_esp:
            conteo_esp[esp] += 1
        else:
            conteo_esp[esp] = 1

    print(f"\n  Total de citas registradas : {total}")
    print(f"  ─ Pendientes               : {pendientes}")
    print(f"  ─ Confirmadas              : {confirmadas}")
    print(f"  ─ Canceladas               : {canceladas}")

    if len(conteo_esp) > 0:
        print("\n  Citas por especialidad:")
        for esp, cantidad in conteo_esp.items():
            print(f"    • {esp:<22}: {cantidad}")

    pausar()


# ─────────────────────────────────────────────
#   MENÚ PRINCIPAL
# ─────────────────────────────────────────────

def menu_principal():
    """Muestra el menú principal y gestiona la navegación."""
    while True:
        limpiar_pantalla()
        mostrar_linea()
        print("     🏥  SISTEMA DE AGENDA MÉDICA  🏥")
        mostrar_linea()
        print()
        print("    1.  Agendar nueva cita")
        print("    2.  Ver todas las citas")
        print("    3.  Buscar citas por cédula")
        print("    4.  Actualizar estado de cita")
        print("    5.  Eliminar cita")
        print("    6.  Ver resumen estadístico")
        print("    0.  Salir")
        print()
        mostrar_linea()

        opcion = input("    Seleccione una opción: ").strip()

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
            ver_resumen()
        elif opcion == "0":
            limpiar_pantalla()
            print("\n  Gracias por usar el Sistema de Agenda Médica.")
            print("  ¡Hasta luego!\n")
            break
        else:
            print("\n  ⚠  Opción inválida. Intente de nuevo.")
            pausar()


# ─────────────────────────────────────────────
#   PUNTO DE ENTRADA DEL PROGRAMA
# ─────────────────────────────────────────────

if __name__ == "__main__":
    menu_principal()