from FuncionesPrueba4 import *
limpiar()

estudiantes = []

while True:
    limpiar()
    mostrarMenu()
    opcion = obtenerOpcion()
    
    if opcion == 1:
        limpiar()
        agregarEstudiante(estudiantes)
        pausar()
        
    elif opcion == 2:
        limpiar()
        nombre = input("Ingrese el Nombre del Estudiante que desee buscar:\n").strip()
        posicion = buscarEstudiante(estudiantes, nombre)
        if posicion != -1:
            print(f"Estudiante encontrado en la posición {posicion}.")
            print(estudiantes[posicion])
        else:
            print("No existen estudiantes con ese Nombre.")
        pausar()

    elif opcion == 3:
        limpiar()
        if len(estudiantes) > 0:
            nombre = input("Ingrese el Nombre del Estudiante que desea eliminar:\n").strip() 
            posicion = buscarEstudiante(estudiantes, nombre)
            if posicion != -1:
                estudiantes.pop(posicion)
                print("El estudiante ha sido eliminado del registro.")
            else:
                print(f"El estudiante '{nombre}' no se encuentra registrado.")
        else:
            print("No existen estudiantes Registrados.")
        pausar()
        
    elif opcion == 4:
        limpiar()
        if len(estudiantes) > 0:
            actualizarEstado(estudiantes)
            print("Estados actualizados correctamente.")
        else:
            print("No existen estudiantes Registrados.")
        pausar()
        
    elif opcion == 5:
        limpiar()
        mostrarEstudiante(estudiantes)
        input("Presione enter para volver al Menú...\n")
        
    elif opcion == 6:
        limpiar()
        print("Gracias por usar el sistema. Vuelva Pronto")
        break
