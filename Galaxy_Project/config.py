import os

def load_config(path='config.txt'):
    # Garantiza la lectura del archivo en la misma carpeta que el ejecutable
    if not os.path.isabs(path):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(script_dir, path)

    config = {}
    with open(path, 'r') as file:
        for line in file:
            line_clean = line.strip()
            if not line_clean or line_clean.startswith('#'):
                continue
            parameter, value = line_clean.split("=")
            parameter = parameter.strip()
            value = value.strip()
            
            if ',' in value:
                config[parameter] = tuple(int(c.strip()) for c in value.split(","))
            elif '.' in value:
                config[parameter] = float(value)
            else:
                config[parameter] = int(value)
    return config 