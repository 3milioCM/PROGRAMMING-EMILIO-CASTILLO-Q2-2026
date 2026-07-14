from PIL import Image
import os
import logging

# Configuración de logs
if not os.path.exists('logs'): os.makedirs('logs')
logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s — %(message)s')

def main():
    # 1. Carga de configuración
    config = {}
    try:
        with open("config.txt", 'r') as archivo:
            for linea in archivo:
                if "=" in linea:
                    clave, valor = linea.strip().split("=")
                    config[clave.strip()] = float(valor.strip()) if "." in valor else int(valor.strip())
    except FileNotFoundError:
        print("Error: No se encontró 'config.txt'.")
        return

    # 2. Lectura y validación de datos
    try:
        if not os.path.exists("clase.csv"):
            print("Error: No se encontró 'clase.csv'. Asegúrate de generar el fractal primero.")
            return

        with open("clase.csv", 'r') as data:
            datos = data.readlines()
        
        if len(datos) <= 1:
            print("Error: El archivo 'clase.csv' está vacío o no tiene datos.")
            return

        alto, ancho, max_iter = config["alto"], config["ancho"], config["max_iter"]
        img = Image.new("HSV", (ancho, alto))
        
        # Saltar encabezados y procesar filas
        encabezados = datos.pop(0)
        for dato in datos:
            try:
                fila, columna, iteraciones = map(int, dato.strip().split(","))
                # Validación de rango
                brillo = 0 if (iteraciones == max_iter) else int((iteraciones / max_iter) * 255)
                img.putpixel((columna, fila), (brillo, 255, 255))
            except ValueError:
                continue # Saltar líneas mal formadas

        # 3. Conversión y guardado
        img_rgb = img.convert('RGB')
        img_rgb.save("mandelbrot-clase2.png")
        print("DONE: Imagen 'mandelbrot-clase2.png' guardada con éxito.")
        logging.info("Imagen generada correctamente.")

    except Exception as e:
        print(f"Ocurrió un error al generar la imagen: {e}")
        logging.error(f"Error en visualización: {e}")

if __name__ == "__main__":
    main() 