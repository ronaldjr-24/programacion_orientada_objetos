import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'UNIDAD_1/1.2_tecnicas_de_Programacion/Ejemplos_de_tecnicas_programacion.py',
        '2': 'UNIDAD_1/el_promedio_semanal_del_clima/Programación_Orientada_a_Objetos.py',
        '3': 'UNIDAD_1/situaciones_del_mundo_real/Ejemplos_del_Mundo_Real.py',
        '4': 'UNIDAD_2/Desarrollo_de_un_pequeño_programa/Tipos_de_datos.py',
        '5': 'UNIDAD_2/Aplicacion_de_Conceptos_de_POO/Definición_de_Objeto_H_E_P.py',
        '6': 'UNIDAD_2/Constructores_y_Destructores/concepto_sobre_constructores_y_destructores.py'
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()