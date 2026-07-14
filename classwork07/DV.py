import logging
import os

if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s — [%(levelname)s] %(message)s'
)

def calcular_digito_verificador(rol_num):
    rol_invertido = str(rol_num)[::-1]
    suma = 0
    multiplicador = 2
    for digito in rol_invertido:
        suma += int(digito) * multiplicador
        multiplicador = 2 if multiplicador == 7 else multiplicador + 1
    modulo = suma % 11
    dv = 11 - modulo
    if dv == 11: return 0
    if dv == 10: return 'K'
    return dv

def main():
    entrada = input("INPUT: ").strip()
    if entrada.count('-') != 1:
        print("Rol inválido: No tiene el formato XXXXXXXXX-X")
        return
    rol_num, dv_usuario = entrada.split('-')
    if not rol_num.isdigit():
        print("Los digitos del rol deben ser numéricos")
        return
    if not (dv_usuario.isdigit() or dv_usuario.upper() == 'K'):
        print("El digito verificador debe ser numérico")
        return
    dv_calculado = calcular_digito_verificador(rol_num)
    if str(dv_calculado) == dv_usuario.upper():
        print(f"{rol_num}-{dv_usuario.upper()}")
        logging.info(f"Éxito: {entrada}")
    else:
        print(f"Error: El dígito verificador no conicide, se esperaba {dv_calculado}")
        logging.error(f"Mismatch: {entrada}, esperado {dv_calculado}")

if __name__ == "__main__":
    main()

