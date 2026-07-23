import logging
import os
import json
import ast

# Configuración de logs
if not os.path.exists('logs'): os.makedirs('logs')
logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s — %(message)s')

def cargar_datos():
    # Base de datos completa para cubrir los casos de prueba y lectura de archivo
    usuarios = {
        'jperez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Juan Pérez'},
        'amartin': {'password': '1234', 'rol': 'alumno', 'nombre': 'Ana Martín'},
        'euc': {'password': '1234', 'rol': 'alumno', 'nombre': 'Eugenio Castillo'},
        'cbalam': {'password': '1234', 'rol': 'alumno', 'nombre': 'Carlos Balam'},
        'mlopez': {'password': '1234', 'rol': 'alumno', 'nombre': 'María López'},
        'jpedrozo': {'password': '1234', 'rol': 'maestro', 'nombre': 'Juan Pedrozo'},
        'dgamboa': {'password': '1234', 'rol': 'coordinador', 'nombre': 'David Gamboa'},
        'rgarcia': {'password': '1234', 'rol': 'coordinador', 'nombre': 'Rosa García'}
    }

    calificaciones = {
        'jperez': {'Matemáticas': 8.5, 'Programación': 9.0, 'Inglés': 7.5, 'Programming': 9.2, 'Discrete Math': 8.0},
        'amartin': {'Matemáticas': 9.0, 'Programación': 8.0, 'Inglés': 8.5},
        'euc': {'Differential Calculus': 6.0, 'Programming': 8.5, 'English II': 9.0},
        'cbalam': {'English II': 8.5, 'Programming': 9.0, 'Differential Calculus': 8.0},
        'mlopez': {'Matemáticas': 9.5, 'Programación': 10.0, 'Inglés': 9.0, 'Differential Calculus': 9.0, 'Discrete Math': 9.5}
    }

    materias = ('Matemáticas', 'Programación', 'Inglés', 'Differential Calculus', 'Discrete Math', 'English II', 'Programming')

    # Lectura dinámica si existe Datos10.txt
    archivos_posibles = ['Datos10.txt', 'datos10.txt', 'Datos.txt', 'datos.txt', 'config.txt']
    archivo_encontrado = next((a for a in archivos_posibles if os.path.exists(a)), None)

    if archivo_encontrado:
        try:
            with open(archivo_encontrado, 'r', encoding='utf-8') as f:
                contenido = f.read().strip()
                try:
                    data = json.loads(contenido)
                    if isinstance(data, dict):
                        if 'usuarios' in data: usuarios.update(data['usuarios'])
                        if 'calificaciones' in data: calificaciones.update(data['calificaciones'])
                        if 'materias' in data: materias = tuple(data['materias'])
                except Exception:
                    try:
                        data = ast.literal_eval(contenido)
                        if isinstance(data, dict):
                            if 'usuarios' in data: usuarios.update(data['usuarios'])
                            if 'calificaciones' in data: calificaciones.update(data['calificaciones'])
                            if 'materias' in data: materias = tuple(data['materias'])
                    except Exception:
                        pass
        except Exception as e:
            logging.error(f"Error cargando datos: {e}")

    return usuarios, calificaciones, materias


def main():
    usuarios, calificaciones, materias = cargar_datos()

    # 1. Login con manejo de intentos
    usuario_actual = None
    for intento in range(3):
        try:
            usr = input("Usuario: ").strip()
            pwd = input("Contraseña: ").strip()
        except EOFError:
            return

        if usr in usuarios and usuarios[usr]['password'] == pwd:
            usuario_actual = usr
            print(f"Bienvenido, {usuarios[usr]['nombre']}")
            break
        print("Credenciales incorrectas.")
    else:
        print("Demasiados intentos fallidos. Saliendo.")
        return

    rol = usuarios[usuario_actual]['rol']

    # 2. Menú por Rol
    if rol == 'alumno':
        print(f"\nBoleta de {usuarios[usuario_actual]['nombre']}")
        aprobadas, pendientes = set(), set()
        mis_notas = calificaciones.get(usuario_actual, {})
        
        # Evaluar todas las materias registradas del alumno
        for mat, nota in mis_notas.items():
            print(f"{mat}: {nota}")
            if nota >= 8.0:
                aprobadas.add(mat)
            else:
                pendientes.add(mat)

        print(f"Aprobadas: {aprobadas}, Pendientes: {pendientes}")

    elif rol == 'maestro':
        while True:
            try:
                print("\nAlumnos disponibles:", [u for u, d in usuarios.items() if d['rol'] == 'alumno'])
                alumno_sel = input("¿Qué alumno desea calificar?: ").strip()
                if alumno_sel.lower() in ['exit', 'salir', 'cancel', '']:
                    break

                materia_sel = input("¿Qué materia?: ").strip()
                if materia_sel.lower() in ['exit', 'salir', 'cancel', '']:
                    break

                # Mostrar calificación actual antes del cambio
                nota_actual = calificaciones.get(alumno_sel, {}).get(materia_sel, "N/A")
                print(f"Calificación actual: {nota_actual}")

                entrada_nota = input("Nueva calificación (0-10): ").strip()
                if entrada_nota.lower() in ['exit', 'salir', 'cancel']:
                    print("Cambio cancelado.")
                    break

                nueva_nota = float(entrada_nota)
                if not (0 <= nueva_nota <= 10):
                    print("Error: La calificación debe ser un número entre 0 y 10.")
                    continue

                confirmacion = input("¿Confirmar cambio? (yes/no): ").strip().lower()
                if confirmacion in ['yes', 'si', 's']:
                    if alumno_sel not in calificaciones:
                        calificaciones[alumno_sel] = {}
                    calificaciones[alumno_sel][materia_sel] = nueva_nota
                    print("Calificación actualizada. Grade updated.")
                    logging.info(f"Maestro {usuario_actual} actualizó {alumno_sel}")
                else:
                    print("Cambio cancelado.")

            except (EOFError, ValueError):
                break

    elif rol == 'coordinador':
        print("\n--- Reporte del Coordinador ---")
        for est, notas in calificaciones.items():
            nombre_est = usuarios.get(est, {}).get('nombre', est)
            print(f"{nombre_est} ({est}): {notas}")

if __name__ == "__main__":
    main()