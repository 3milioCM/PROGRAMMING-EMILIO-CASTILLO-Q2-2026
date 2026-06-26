# Datos iniciales
materias = ('Matemáticas', 'Programación', 'Inglés')

usuarios = {
    'jperez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Juan Pérez'},
    'amartin': {'password': '1234', 'rol': 'alumno', 'nombre': 'Ana Martín'},
    'est1': {'password': '1234', 'rol': 'alumno', 'nombre': 'Estudiante 3'},
    'est2': {'password': '1234', 'rol': 'alumno', 'nombre': 'Estudiante 4'},
    'est3': {'password': '1234', 'rol': 'alumno', 'nombre': 'Estudiante 5'},
    'est4': {'password': '1234', 'rol': 'alumno', 'nombre': 'Estudiante 6'},
    'mlopez': {'password': '1234', 'rol': 'maestro', 'nombre': 'María López'},
    'rgarcia': {'password': '1234', 'rol': 'coordinador', 'nombre': 'Rosa García'}
}

calificaciones = {
    'jperez': {'Matemáticas': 8.5, 'Programación': 9.0, 'Inglés': 7.5},
    'amartin': {'Matemáticas': 9.0, 'Programación': 8.0, 'Inglés': 8.5},
    'est1': {'Matemáticas': 7.0, 'Programación': 7.0, 'Inglés': 7.0},
    'est2': {'Matemáticas': 9.5, 'Programación': 9.5, 'Inglés': 9.5},
    'est3': {'Matemáticas': 6.0, 'Programación': 6.0, 'Inglés': 6.0},
    'est4': {'Matemáticas': 8.0, 'Programación': 8.0, 'Inglés': 8.0}
}

# 1. Login
usuario_actual = None
while True:
    usr = input("Usuario: ")
    pwd = input("Contraseña: ")
    
    if usr in usuarios and usuarios[usr]['password'] == pwd:
        usuario_actual = usr
        print(f"Bienvenido, {usuarios[usr]['nombre']} ({usuarios[usr]['rol']})")
        break
    else:
        print("Credenciales incorrectas. Intente de nuevo.")

# 3. Menú por Rol
rol = usuarios[usuario_actual]['rol']

if rol == 'alumno':
    print(f"\nBoleta de {usuarios[usuario_actual]['nombre']}")
    aprobadas = set()
    pendientes = set()
    
    for mat in materias:
        nota = calificaciones[usuario_actual][mat]
        print(f"{mat}: {nota}")
        if nota >= 8.0:
            aprobadas.add(mat)
        else:
            pendientes.add(mat)
            
    print(f"Materias aprobadas: {aprobadas}")
    print(f"Materias pendientes: {pendientes}")

elif rol == 'maestro':
    print("\nLista de alumnos:")
    for user_key, data in usuarios.items():
        if data['rol'] == 'alumno':
            print(f"- {user_key} ({data['nombre']})")
            
    alumno_sel = input("¿Qué alumno desea calificar (usuario)?: ")
    materia_sel = input("¿Qué materia desea calificar?: ")
    
    if alumno_sel in calificaciones and materia_sel in materias:
        nueva_nota = float(input("Nueva calificación: "))
        calificaciones[alumno_sel][materia_sel] = nueva_nota
        print("Calificación actualizada.")
    else:
        print("Error: Usuario o materia no válidos.")

elif rol == 'coordinador':
    print("\n--- Reporte del Coordinador ---")
    print("Profesores:")
    for k, v in usuarios.items():
        if v['rol'] == 'maestro': print(f"- {v['nombre']}")
    
    print(f"\nMaterias: {materias}")
    
    print("\nCalificaciones de todos los alumnos:")
    for est, notas in calificaciones.items():
        print(f"{usuarios[est]['nombre']}: {notas}")