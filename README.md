# Flux: Productivity Intelligence

Flux es un sistema inteligente diseñado para la gestión y priorización de tareas académicas, permitiendo a los estudiantes organizar sus sesiones de estudio mediante una lógica de procesamiento automatizada.

## Estructura del Proyecto
- `/assets`: Contiene el diagrama de flujo (`flux_flowchart.png`) que ilustra la lógica del sistema.
- `/docs`: Incluye el pseudocódigo detallado (`pseudocode.md`) del algoritmo.
- `/logs`: Directorio de auditoría donde se generan los registros de ejecución (`app.log`) en tiempo real.
- `main.py`: Script principal de la aplicación en Python.

## Características
- **Priorización Automática**: Clasifica tareas por nivel de urgencia (Alta/Media/Baja).
- **Sistema de Auditoría**: Registro automático de eventos, entradas de usuario y errores mediante el módulo `logging`.
- **Diseño Modular**: Lógica clara basada en un esquema IPO (Input, Process, Output).

## Ejecución
Para ejecutar el sistema Flux:
1. Asegúrate de tener instalado Python 3.x.
2. Clona este repositorio.
3. Ejecuta el programa en tu terminal:
   ```bash
   python main.py

