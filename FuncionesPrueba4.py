import os, time

estudiantes = []

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    time.sleep(3)

def validarNombre(nombre):
    if len(nombre.strip()) > 0:
        return True
    return False

def validarEdad(edad):
    if edad > 0:
        return True
    return False

def validarNota(nota):
    if 1.0 <= float(nota) <= 7.0:
        return True
    return False

def mostrarMenu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar estudiante.")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Actualizar estados")
    print("5. Mostrar estudiantes")
    print("6. Salir")

def obtenerOpcion():
    try:
        opcion = int(input("Ingrese una Opción\n"))
        if 1 <= opcion <= 6:
            return opcion
        else:
            print("La opcion ingresada no Existe.")
    except:
        print("La opción ingresada debe ser númerica.")
    return -1

def agregarEstudiante(estudiantes):
    while True:
        nombre = input("Ingrese el Nombre del estudiante:\n").strip()
        if validarNombre(nombre):
            break
        else:
            print("El nombre no puede estar vacío.")
            
    while True:
        try:
            edad = int(input("Ingrese la Edad:\n"))
            if validarEdad(edad):
                break
            else:
                print("La edad debe ser un número entero mayor a 0.")
        except ValueError:
            print("La edad debe ser un valor numérico entero.")
            
    while True:
        try:
            nota = float(input("Ingrese la Nota (1.0 a 7.0):\n"))
            if validarNota(nota):
                break
            else:
                print("La nota de la asignatura debe estar en el rango de 1.0 a 7.0.")
        except ValueError:
            print("La nota debe ser un valor numérico decimal.")

    estudiante = {
        "Nombre": nombre,
        "Edad": edad,
        "Nota": nota,
        "Aprobado": False
    }
    
    estudiantes.append(estudiante)
    print("¡Estudiante agregado con Éxito!")

def buscarEstudiante(estudiantes, nombre):
    if len(estudiantes) > 0:
        for e in range(len(estudiantes)):
            if estudiantes[e]["Nombre"].lower() == nombre.lower():
                return e
        return -1
    else:
        return -1

def actualizarEstado(estudiantes):
    for e in estudiantes:
        if e["Nota"] >= 4.0:
            e["Aprobado"] = True
        else:
            e["Aprobado"] = False

def mostrarEstudiante(estudiantes):
    if len(estudiantes) > 0:
        actualizarEstado(estudiantes)
        print("=== LISTA DE ESTUDIANTES ===")
        for e in estudiantes:
            print(f"Nombre: {e['Nombre']}")
            print(f"Edad: {e['Edad']}")
            print(f"Nota: {e['Nota']}")
            estado = "APROBADO" if e["Aprobado"] else "REPROBADO"
            print(f"Estado: {estado}")
            print("********************************************")
    else:
        print("No existen estudiantes registrados.")

    
