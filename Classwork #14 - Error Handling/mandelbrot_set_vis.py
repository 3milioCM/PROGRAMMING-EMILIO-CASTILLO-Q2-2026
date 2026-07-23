import os
import logging
import colorsys
import struct
import zlib

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

# Configuración de logs
if not os.path.exists('logs'): os.makedirs('logs')
logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s — %(message)s')

def guardar_png_nativo(ancho, alto, matriz_rgb, filename="mandelbrot.png"):
    """Genera una imagen PNG válida utilizando únicamente la librería estándar de Python."""
    raw_data = bytearray()
    for y in range(alto):
        raw_data.append(0)  # Filtro PNG 0 (None)
        for x in range(ancho):
            r, g, b = matriz_rgb[y][x]
            raw_data.extend([r, g, b])
    
    png_header = b'\x89PNG\r\n\x1a\n'
    ihdr_data = struct.pack('>IIBBBBB', ancho, alto, 8, 2, 0, 0, 0)
    ihdr_crc = zlib.crc32(b'IHDR' + ihdr_data)
    ihdr_chunk = struct.pack('>I', len(ihdr_data)) + b'IHDR' + ihdr_data + struct.pack('>I', ihdr_crc)
    
    compressed_data = zlib.compress(raw_data)
    idat_crc = zlib.crc32(b'IDAT' + compressed_data)
    idat_chunk = struct.pack('>I', len(compressed_data)) + b'IDAT' + compressed_data + struct.pack('>I', idat_crc)
    
    iend_crc = zlib.crc32(b'IEND')
    iend_chunk = struct.pack('>I', 0) + b'IEND' + struct.pack('>I', iend_crc)
    
    with open(filename, 'wb') as f:
        f.write(png_header + ihdr_chunk + idat_chunk + iend_chunk)

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

    # 2. Lectura de datos
    csv_file = "clase.csv" if os.path.exists("clase.csv") else "mandelbrot.csv"
    if not os.path.exists(csv_file):
        print(f"Error: No se encontró '{csv_file}'.")
        return

    try:
        with open(csv_file, 'r') as data:
            datos = data.readlines()
        
        if len(datos) <= 1:
            print("Error: El archivo de datos está vacío.")
            return

        alto, ancho, max_iter = int(config["alto"]), int(config["ancho"]), int(config["max_iter"])

        if HAS_PIL:
            img = Image.new("HSV", (ancho, alto))
            datos.pop(0)  # Saltar encabezado
            for dato in datos:
                try:
                    fila, columna, iteraciones = map(int, dato.strip().split(","))
                    brillo = 0 if (iteraciones == max_iter) else int((iteraciones / max_iter) * 255)
                    img.putpixel((columna, fila), (brillo, 255, 255))
                except ValueError:
                    continue
            img_rgb = img.convert('RGB')
            img_rgb.save("mandelbrot.png")
        else:
            # Fallback nativo en caso de que el servidor no tenga PIL instalado
            matriz = [[(0, 0, 0) for _ in range(ancho)] for _ in range(alto)]
            datos.pop(0)  # Saltar encabezado
            for dato in datos:
                try:
                    fila, columna, iteraciones = map(int, dato.strip().split(","))
                    if 0 <= fila < alto and 0 <= columna < ancho:
                        if iteraciones == max_iter:
                            rgb = (0, 0, 0)
                        else:
                            h = iteraciones / max_iter
                            r_f, g_f, b_f = colorsys.hsv_to_rgb(h, 1.0, 1.0)
                            rgb = (int(r_f * 255), int(g_f * 255), int(b_f * 255))
                        matriz[fila][columna] = rgb
                except ValueError:
                    continue
            guardar_png_nativo(ancho, alto, matriz, "mandelbrot.png")

        print("DONE: Imagen 'mandelbrot.png' guardada con éxito.")
        logging.info("Imagen generada correctamente.")

    except Exception as e:
        print(f"Ocurrió un error al generar la imagen: {e}")
        logging.error(f"Error en visualización: {e}")

if __name__ == "__main__":
    main()