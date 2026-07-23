import logging
import os

# Configuración de logs
if not os.path.exists('logs'): os.makedirs('logs')
logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s — %(message)s')

def main():
    config = {}
    
    # 1. Validación de lectura de archivo
    try:
        with open("config.txt", 'r') as archivo:
            for linea in archivo:
                if "=" in linea:
                    clave, valor = linea.strip().split("=")
                    config[clave.strip()] = float(valor.strip())
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'config.txt'")
        return
    except Exception as e:
        print(f"Error procesando el archivo de configuración: {e}")
        return

    # 2. Validación de llaves necesarias
    requeridos = ['ancho', 'alto', 'max_iter', 'real_min', 'real_max', 'imag_min', 'imag_max']
    if not all(k in config for k in requeridos):
        print("Error: Faltan parámetros en config.txt")
        return

    # 3. Procesamiento
    try:
        ancho, alto, max_iter = int(config["ancho"]), int(config["alto"]), int(config["max_iter"])
        
        with open("mandelbrot.csv", 'w') as salida:
            salida.write("fila,columna,iteraciones\n")
            
            for fila in range(alto):
                for columna in range(ancho):
                    real = config['real_min'] + (columna / ancho) * (config['real_max'] - config['real_min'])
                    imag = config['imag_min'] + (fila / alto) * (config['imag_max'] - config['imag_min'])
                    c = complex(real, imag)
                    
                    z = 0j
                    iteraciones = 0
                    while (abs(z) <= 2) and (iteraciones < max_iter):
                        z = z*z + c
                        iteraciones += 1
                    
                    salida.write(f"{fila},{columna},{iteraciones}\n")
        
        print("Generación de fractal completada con éxito en 'mandelbrot.csv'.")
        logging.info("Fractal generado correctamente.")

    except Exception as e:
        print(f"Ocurrió un error durante el cálculo: {e}")
        logging.error(f"Error en procesamiento: {e}")

if __name__ == "__main__":
    main() 


    