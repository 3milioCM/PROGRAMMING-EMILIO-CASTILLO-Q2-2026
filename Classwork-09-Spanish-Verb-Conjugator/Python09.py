# Definición de estructuras de datos requeridas
pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

# 1. Input: Pedir el verbo al usuario
verbo = input("Ingrese verbo: ").lower().strip()

# 2. Process: Obtener raíz y terminación usando slicing
raiz = verbo[:-2]
final = verbo[-2:]

# 3. Output: Validación y conjugación
if final in terminaciones:
    lista_conjugaciones = terminaciones[final]
    
    for i in range(len(pronombres)):
        print(f"{pronombres[i]} {raiz}{lista_conjugaciones[i]}")
else:
    print("Error: El verbo debe terminar en 'ar', 'er' o 'ir'.")