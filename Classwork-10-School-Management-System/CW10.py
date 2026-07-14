import logging
import os

# Configuración de logs
if not os.path.exists('logs'): os.makedirs('logs')
logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s — %(message)s')

usuarios = {
    'jperez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Juan Pérez'},
    'amartin': {'password': '1234', 'rol': 'alumno', 'nombre': 'Ana Martín'},
    'mlopez': {'password': '1234', 'rol': 'maestro', 'nombre': 'María López'},
    'rgarcia': {'password': '1234', 'rol': 'coordinador', 'nombre': 'Rosa García'}
}

calificaciones = {
    'jperez': {'Matemáticas': 8.5, 'Programación': 9.0, 'Inglés': 7.5},
    'amartin': {'Matemáticas': 9.0, 'Programación': 8.0, 'Inglés': 8.5}
}
materias = ('Matemáticas', 'Programación', 'Inglés')

def main():
    # 1. Login con manejo de intentos
    usuario_actual = None
    for intento in range(3):
        usr = input("Usuario: ").strip()
        pwd = input("Contraseña: ").strip()
        if usr in usuarios and usuarios[usr]['password'] == pwd:
            usuario_actual = usr
            print(f"Bienvenido, {usuarios[usr]['nombre']}")
            break
        print("Credenciales incorrectas.")
    else:
        print("Demasiados intentos fallidos. Saliendo."); return

    rol = usuarios[usuario_actual]['rol']

    # 2. Menú por Rol con validaciones
    if rol == 'alumno':
        print(f"\nBoleta de {usuarios[usuario_actual]['nombre']}")
        aprobadas, pendientes = set(), set()
        for mat in materias:
            nota = calificaciones[usuario_actual].get(mat, 0.0)
            print(f"{mat}: {nota}")
            if nota >= 8.0: aprobadas.add(mat)
            else: pendientes.add(mat)
        print(f"Aprobadas: {aprobadas}, Pendientes: {pendientes}")

    elif rol == 'maestro':
        print("\nAlumnos disponibles:", [u for u, d in usuarios.items() if d['rol'] == 'alumno'])
        alumno_sel = input("¿Qué alumno desea calificar?: ").strip()
        materia_sel = input("¿Qué materia?: ").strip()
        
        if alumno_sel in calificaciones and materia_sel in materias:
            try:
                nueva_nota = float(input("Nueva calificación (0-10): "))
                if not (0 <= nueva_nota <= 10): raise ValueError
                calificaciones[alumno_sel][materia_sel] = nueva_nota
                print("Calificación actualizada.")
                logging.info(f"Maestro {usuario_actual} actualizó {alumno_sel}")
            except ValueError:
                print("Error: La calificación debe ser un número entre 0 y 10.")
        else:
            print("Error: Usuario o materia no válidos.")

    elif rol == 'coordinador':
        print("\n--- Reporte del Coordinador ---")
        for est, notas in calificaciones.items():
            print(f"{usuarios[est]['nombre']}: {notas}")

if __name__ == "__main__":
    main() 