def calcular_digito_verificador(rol):
    # 1. Obtener el rol sin guion ni dígito verificador
    # Convertimos a string por seguridad y quitamos cualquier espacio
    rol_str = str(rol).replace("-", "").strip()
    
    # 2. Invertir el número
    rol_invertido = rol_str[::-1]
    
    # 3. Multiplicar por la secuencia 2, 3, 4, 5, 6, 7
    suma = 0
    multiplicador = 2
    
    for digito in rol_invertido:
        suma += int(digito) * multiplicador
        
        # Incrementar multiplicador y reiniciar si pasa de 7
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
            
    # 4. Obtener el módulo 11 del resultado
    modulo = suma % 11
    
    # 5. Restar el resultado de 11
    digito_verificador = 11 - modulo
    
    # Manejo de casos especiales (opcional pero recomendado):
    # Si el resultado es 11, el dígito suele ser 0
    # Si el resultado es 10, el dígito suele ser 'K'
    if digito_verificador == 11:
        return 0
    elif digito_verificador == 10:
        return 'K'
    else:
        return digito_verificador

# Ejemplo de uso:
rol_input = "201012341"
dv = calcular_digito_verificador(rol_input)
print(f"El dígito verificador para {rol_input} es: {dv}")
print(f"El rol completo es: {rol_input}-{dv}")
