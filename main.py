# Sistema básico de registro de estudiantes

estudiantes = []

def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    carrera = input("Ingrese la carrera: ")
    edad = int(input("Ingrese la edad: "))

    estudiante = {
        "nombre": nombre,
        "carrera": carrera,
        "edad": edad
    }

    estudiantes.append(estudiante)
    print("Estudiante registrado correctamente.")


def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        print("\n--- LISTA DE ESTUDIANTES ---")
        for estudiante in estudiantes:
            print("Nombre:", estudiante["nombre"])
            print("Carrera:", estudiante["carrera"])
            print("Edad:", estudiante["edad"])
            print("------------------------")


def menu():
    while True:
        print("\n=== SISTEMA DE ESTUDIANTES ===")
        print("1. Registrar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            print("Programa finalizado.")
            break
        else:
            print("Opción incorrecta.")


menu()