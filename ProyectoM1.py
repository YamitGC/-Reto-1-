# Proyecto M1 - Gestión de Experimentos
# Este programa permite gestionar experimentos, incluyendo agregar, ver, actualizar resultados, generar informes y eliminar experimentos.
from datetime import *
import os

experimentos = [] # Lista para almacenar los experimentos

# Función principal que muestra el menú de opciones y permite al usuario interactuar con el programa
def menu():
    while True:
        print("Menu de opciones:")
        print("1.Agregar Experimento")
        print("2.Ver Experimento")
        print("3.Actualizar Resultado")
        print("4.Genear Informe")
        print("5.Eliminar Experimento")
        print("6.Salir")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_experimento()
        elif opcion == "2":
            ver_experimento()
        elif opcion == "3":
            actualizar_resultado()    
        elif opcion == "4":
            generar_informe()    
        elif opcion == "5":
            eliminar_experimento()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def limpiar_pantalla():
    # Función para limpiar la pantalla
    os.system("cls" if os.name == "nt" else "clear")

def validar_fecha(fecha):
    # Validar el formato de la fecha ingresada por el usuario y el rango de año
    try:
        fecha_dt = datetime.strptime(fecha, "%d-%m-%Y")
        if 1900 <= fecha_dt.year <= 2025:
            return True
        else:
            print("El año debe estar entre 1900 y 2025.")
            return False
    except ValueError:
        print("Fecha no válida. Debe estar en formato DD-MM-AAAA.")
        return False

def validar_tipo(tipo):
    # Validar el tipo de experimento ingresado por el usuario
    tipos_validos = ["Química", "Biología", "Física"]
    if tipo in tipos_validos:
        return True
    else:
        print("Tipo no válido. Debe ser Química, Biología o Física.")
        return False

def validar_resultados(resultados):
    # Validar los resultados ingresados por el usuario
    try:
        resultados = [float(x) for x in resultados.split(",")]
        return True
    except ValueError:
        print("Resultados no válidos. Deben ser números separados por comas.")
        return False
    
def agregar_experimento():
    limpiar_pantalla()
    # Código para agregar un nuevo experimento
    
    nombre = input("Ingrese el nombre del experimento: ")
    
    fecha = input("Ingrese la fecha del experimento (DD-MM-AAAA): ")
    while not validar_fecha(fecha):
        fecha = input("Ingrese la fecha del experimento (DD-MM-AAAA): ")
        
    tipo = input("Ingrese el tipo de experimento (Química, Biología, Física): ")
    while not validar_tipo(tipo):
        tipo = input("Ingrese el tipo de experimento (Química, Biología, Física): ")
        
    resultados_exp = input("Ingrese los datos experimentales (datos numericos separados por comas): ")
    resultados = validar_resultados(resultados_exp)
    while resultados is None:
        print("Error: Resultados inválidos. Deben ser números separados por comas.")
        resultados_exp = input("Ingrese los resultados numéricos separados por comas (ej. 10,20,30): ")
        resultados = validar_resultados(resultados_exp)
    
    # Crear un diccionario para almacenar los datos del experimento
    experimento = {
        "nombre": nombre,
        "fecha": fecha,
        "tipo": tipo,
        "resultados": resultados_exp
    } 
    
    experimentos.append(experimento) # Agregar el experimento a la lista
    print("Experimento agregado exitosamente.")
    

def ver_experimento():
    limpiar_pantalla()
    # Código para ver los experimentos existentes
    if not experimentos:
        print("No hay experimentos registrados.")
        return
    print("Lista de experimentos:")
    for experimento in experimentos:
        print("-" * 20)
        print(f"Nombre: {experimento['nombre']}")
        print(f"Fecha: {experimento['fecha']}")
        print(f"Tipo: {experimento['tipo']}")
        print(f"Resultados: {experimento['resultados']}")
        print("-" * 20)
        print()

def actualizar_resultado():
    limpiar_pantalla()
    # Código para actualizar el resultado de un experimento
    if not experimentos:
        print("No hay experimentos registrados.")
        return
    
    nombre_a_actualizar = input("Ingrese el nombre del experimento a actualizar: ")
    experimento_encontrado = None
    for experimento in experimentos:
        if experimento["nombre"] == nombre_a_actualizar:
            experimento_encontrado = experimento
            break
        
    if experimento_encontrado is None:
        print(f"No se encontró el experimento con nombre '{nombre_a_actualizar}'.")
        return
    
    nuevos_resultados = input("Ingrese los nuevos resultados (números separados por comas): ")
    while not validar_resultados(nuevos_resultados):
        print("Error: Resultados inválidos. Deben ser números separados por comas.")
        nuevos_resultados = input("Ingrese los nuevos resultados (números separados por comas): ")
        
    experimento_encontrado["resultados"] = nuevos_resultados
    print("Resultados actualizados exitosamente.")
    
def calcular_promedio(resultados):
    # Calcular el promedio de los resultados
    resultados = [float(x) for x in resultados.split(",")]
    return sum(resultados) / len(resultados)

def generar_informe():
    limpiar_pantalla()
    # Código para generar un informe de los experimentos
    if not experimentos:
        print("No hay experimentos registrados.")
        return
    informe = "INFORME DE EXPERIMENTOS\n"
    fecha_actual = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    informe += f"Fecha de generación: {fecha_actual}\n"
    informe += "-" * 20 + "\n"
    
    informe += "DETALLE DE EXPERIMENTOS:\n\n"
    for experimento in experimentos:
        informe += f"Nombre: {experimento['nombre']}\n"
        informe += f"Fecha: {experimento['fecha']}\n"
        informe += f"Tipo: {experimento['tipo']}\n"
        informe += f"Resultados: {experimento['resultados']}\n"
        promedio = calcular_promedio(experimento["resultados"])
        informe += f"Promedio de resultados: {promedio:.2f}\n"
        informe += "-" * 20 + "\n"
        
    informe += "CONCLUSIONES:\n\n"
    informe += "No se incluyen conclusiones en esta versión.\n"
    
    nombre_archivo = input("Ingrese el nombre del archivo para guardar el informe (ej. informe.txt): ")
    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.write(informe)
        print(f"Informe generado exitosamente y guardado como '{nombre_archivo}'.")
        
    except Exception as e:
        print(f"Error al guardar el informe: {e}")
    
def eliminar_experimento():
    limpiar_pantalla()
    # Código para eliminar un experimento
    if not experimentos:
        print("No hay experimentos registrados.")
        return
    
    nombre_a_eliminar = input("Ingrese el nombre del experimento a eliminar: ")
    
    indice_a_eliminar = -1 
    for i, experimento in enumerate(experimentos):
        if experimento["nombre"] == nombre_a_eliminar:
            indice_a_eliminar = i
            break
    
    if indice_a_eliminar == -1:
        print(f"No se encontró el experimento con nombre '{nombre_a_eliminar}'.")
        return
    
    experimentos.pop(indice_a_eliminar)
    print(f"Experimento {nombre_a_eliminar} eliminado exitoamente.)")

if __name__ == "__main__":
    menu()