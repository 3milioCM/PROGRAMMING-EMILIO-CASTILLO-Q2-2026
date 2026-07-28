def recursiva(n):
    try:
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError("Introduce un numero entero")
        if n < 0:
            raise ValueError("El numero no debe ser negativo")
        if n == 0:
            return "Done"
        else:
            print(n)
            return recursiva(n - 1)
    except (TypeError, ValueError) as e:
        print(f"Error en recursiva({n}): {e}")
        return None
def fibonacci(n):
    try:
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError("El índice debe ser un entero.")
        if n < 0:
            raise ValueError("El índice no puede ser negativo.")
        if n == 0 or n == 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    except (TypeError, ValueError) as e:
        print(f"Error en fibonacci({n}): {e}")
        return None
def factorial(n):
    try:
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError("El factorial solo está definido para números enteros.")
        if n < 0:
            raise ValueError("El factorial no está definido para enteros negativos.")
        if n == 0 or n == 1:
            return 1
        else:
            return factorial(n - 1) * n
    except (TypeError, ValueError) as e:
        print(f"Error en factorial({n}): {e}")
        return None
def multiplicacion_recursiva(n, m):
    try:
        if not (isinstance(n, (int, float)) and isinstance(m, int)) or isinstance(n, bool) or isinstance(m, bool):
            raise TypeError("Los operandos deben ser numéricos y 'm' debe ser un entero.")
        if m < 0:
            return -multiplicacion_recursiva(n, -m)
        if m == 0:
            return 0
        else:
            return multiplicacion_recursiva(n, m - 1) + n
    except (TypeError, ValueError) as e:
        print(f"Error en multiplicacion_recursiva({n}, {m}): {e}")
        return None
def division_entera_recursiva(dividendo, divisor):
    try:
        if not (isinstance(dividendo, int) and isinstance(divisor, int)) or isinstance(dividendo, bool) or isinstance(divisor, bool):
            raise TypeError("Ambos valores deben ser números enteros.")
        if divisor == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        if dividendo < 0 and divisor < 0:
            return division_entera_recursiva(-dividendo, -divisor)
        if dividendo < 0:
            return -division_entera_recursiva(-dividendo, divisor)
        if divisor < 0:
            return -division_entera_recursiva(dividendo, -divisor)
        if dividendo - divisor < 0:
            return 0
        else:
            return division_entera_recursiva(dividendo - divisor, divisor) + 1
    except (TypeError, ZeroDivisionError, ValueError) as e:
        print(f"Error en division_entera_recursiva({dividendo}, {divisor}): {e}")
        return None
def potencia_recursiva(base, exponente):
    try:
        if not (isinstance(base, (int, float)) and isinstance(exponente, int)) or isinstance(base, bool) or isinstance(exponente, bool):
            raise TypeError("La base debe ser numérica y el exponente debe ser un entero.")
        if exponente < 0:
            if base == 0:
                raise ZeroDivisionError("Cero no puede ser elevado a un exponente negativo.")
            return 1 / potencia_recursiva(base, -exponente)
        if exponente == 0:
            return 1
        else:
            return potencia_recursiva(base, exponente - 1) * base
    except (TypeError, ZeroDivisionError) as e:
        print(f"Error en potencia_recursiva({base}, {exponente}): {e}")
        return None
def serie_collatz(n):
    try:
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError("El valor inicial debe ser un entero.")
        if n <= 0:
            raise ValueError("La conjetura de Collatz requiere números enteros positivos (n > 0).")
        if n == 1:
            print("END!")
            return 0
        else:
            if n % 2 == 0:
                siguiente = n // 2
            else:
                siguiente = 3 * n + 1
            print(siguiente)
            return serie_collatz(siguiente)
    except (TypeError, ValueError) as e:
        print(f"Error en serie_collatz({n}): {e}")
        return None
def aplanar_json(estructura, clave_padre='', separador='.'):
    elementos = []
    try:
        if isinstance(estructura, list):
            iterador = enumerate(estructura)
        elif isinstance(estructura, dict):
            iterador = estructura.items()
        else:
            return {clave_padre: estructura} if clave_padre else {}
        for key, value in iterador:
            nueva_llave = f"{clave_padre}{separador}{key}" if clave_padre else str(key)
            if isinstance(value, (dict, list)):
                sub_aplanado = aplanar_json(value, nueva_llave, separador)
                elementos.extend(sub_aplanado.items())
            else:
                elementos.append((nueva_llave, value))
        resultado = {}
        for k, v in elementos:
            if k in resultado:
                print(f"Advertencia: Detectada colisión de clave '{k}'. El valor anterior '{resultado[k]}' será sobrescrito por '{v}'.")
            resultado[k] = v
        return resultado
    except Exception as e:
        print(f"Error en aplanar_json: {e}")
        return {}
if __name__ == "__main__":
    print("--- PRUEBAS RECURSIVA ---")
    recursiva(3)
    recursiva(-3)
    print("\n--- PRUEBAS FIBONACCI ---")
    print("Fib(7):", fibonacci(7))
    fibonacci(-1)
    print("\n--- PRUEBAS FACTORIAL ---")
    print("Factorial(5):", factorial(5))
    factorial(1.5)
    print("\n--- PRUEBAS MULTIPLICACIÓN ---")
    print("Mult(4, 3):", multiplicacion_recursiva(4, 3))
    print("Mult(4, -3):", multiplicacion_recursiva(4, -3))
    print("\n--- PRUEBAS DIVISIÓN ENTERA ---")
    print("Div(17, 5):", division_entera_recursiva(17, 5))
    division_entera_recursiva(10, 0)
    print("\n--- PRUEBAS POTENCIA ---")
    print("Potencia(2, 5):", potencia_recursiva(2, 5))
    print("Potencia(2, -2):", potencia_recursiva(2, -2))
    print("\n--- PRUEBAS COLLATZ ---")
    serie_collatz(6)
    serie_collatz(-6)
    print("\n--- PRUEBA APLANAR JSON CON EL DOCUMENTO PROPORCIONADO ---")
    json_prueba = {
        "a": 1,
        "b": {"c": 2, "d": {"e": 3}},
        "f": [1, 2, 3],
        "g": [{"h": 4}, {"i": 5}],
        "j": {"k": [6, 7, {"l": 8}]},
        "m": None,
        "n": True,
        "o": []
    }
    import json
    resultado_plano = aplanar_json(json_prueba)
    print(json.dumps(resultado_plano, indent=2))