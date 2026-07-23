import math
import logging
import os

# Configuración de logs
if not os.path.exists('logs'): os.makedirs('logs')
logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s — %(message)s')

def evaluar_funcion(f_str, x_val):
    try:
        # Validación: solo permitir 'x', números, math, operadores
        if 'y' in f_str or 'z' in f_str: raise ValueError("Variable no permitida")
        if '^' in f_str: raise ValueError("Usa ** para potencias")
        
        # Evaluar
        local_scope = {"x": x_val, "math": math}
        return eval(f_str, {"__builtins__": None}, local_scope)
    except ZeroDivisionError:
        raise ZeroDivisionError
    except Exception:
        raise ValueError("La función ingresada no es válida")

def main():
    try:
        # Inputs
        a_str = input("Límite izquierdo (a): ").strip()
        b_str = input("Límite derecho (b): ").strip()
        f_x = input("Función f(x): ").strip()
        method = input("Método (LRM/RRM/MPM/TM): ").strip()

        # Validación numérica de límites
        try:
            a = float(eval(a_str.replace("pi", "math.pi")))
        except: print("El límite inferior debe ser numérico"); return
        
        try:
            b = float(eval(b_str.replace("pi", "math.pi")))
        except: print("El límite superior debe ser numérico"); return

        # Reglas de negocio
        if a >= b: print("El límite inferior debe ser menor que el límite superior"); return
        if not f_x: print("La función ingresada no es válida"); return
        if "x" not in f_x and f_x != "": print("La función debe estar escrita en términos de x"); return
        if method not in ["LRM", "RRM", "MPM", "TM"]: print("El método de integración no es válido. Usa LRM, RRM, MPM o TM"); return

        # Cálculo
        n = 1000
        h = (b - a) / n
        area = 0.0

        # Verificación de puntos críticos (División entre cero)
        for i in range(n + 1):
            xi = a + i * h
            try: evaluar_funcion(f_x, xi)
            except ZeroDivisionError: print("La función no está definida en algún punto del intervalo"); return

        # Integración
        if method == "TM": # Trapecio
            area = (h / 2) * (evaluar_funcion(f_x, a) + evaluar_funcion(f_x, b))
            for i in range(1, n): area += h * evaluar_funcion(f_x, a + i * h)
        elif method == "LRM":
            for i in range(n): area += h * evaluar_funcion(f_x, a + i * h)
        elif method == "RRM":
            for i in range(1, n + 1): area += h * evaluar_funcion(f_x, a + i * h)
        elif method == "MPM":
            for i in range(n): area += h * evaluar_funcion(f_x, a + (i + 0.5) * h)

        print(f"The integration of {f_x} is {area:.3f}")
        logging.info(f"Éxito: {f_x} en [{a}, {b}] usando {method}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    
    