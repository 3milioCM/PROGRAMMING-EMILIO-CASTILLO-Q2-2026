import logging
import os

# Configuración de logs
if not os.path.exists('logs'): os.makedirs('logs')
logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s — %(message)s')

def main():
    pronombres = ['Yo', 'Tú', 'Él', 'Nosotros', 'Vosotros', 'Ellos']
    terminaciones = {
        'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
        'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
        'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
    }

    # Input crudo para detectar reglas de negocio
    raw_verbo = input("Ingrese verbo: ")

    # Caso 23: Regla de mayúsculas
    if not raw_verbo == raw_verbo.lower():
        print("El verbo debe escribirse en minúsculas")
        return

    # Caso 24: Regla de espacios
    if raw_verbo != raw_verbo.strip():
        print("El verbo no debe tener espacios extra")
        return

    verbo = raw_verbo.strip()

    # Caso 20-22: Validación de longitud y tipo
    if len(verbo) < 3 or not verbo.isalpha():
        print("El verbo debe terminar en ar, er o ir")
        return

    raiz = verbo[:-2]
    final = verbo[-2:]

    # Caso 19: Validación de terminación
    if final not in terminaciones:
        print("El verbo debe terminar en ar, er o ir")
        return

    # Proceso de conjugación
    lista_conjugaciones = terminaciones[final]
    for i in range(len(pronombres)):
        print(f"{pronombres[i]} {raiz}{lista_conjugaciones[i]}")
    
    logging.info(f"Conjugación exitosa: {verbo}")

if __name__ == "__main__":
    main()