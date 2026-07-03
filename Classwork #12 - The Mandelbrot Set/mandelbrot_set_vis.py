from PIL import Image

config = {}

archivo = open("config.txt", 'r')

for linea in archivo:
    clave, valor = linea.strip().split("=")
    config[clave] = float(valor) if "." in valor else int(valor)
archivo.close()


#print(config)
with open("clase.csv", 'r') as data:
    datos = data.readlines() #

alto, ancho, max_iter =config["alto"], config["ancho"], config["max_iter"]

img = Image.new("HSV", (ancho, alto))

#QUITAR ENCABEZADOS
encabezados = datos.pop(0)

#print(encabezados)
for dato in datos:
    fila, columna, iteraciones = map(int, dato.strip().split(","))
    brillo = 0 if (iteraciones == max_iter) else int((iteraciones / max_iter) * 255)
    #putpixel necetia tuplas, la primera me indica la posición y la segunda el color
    img.putpixel((columna, fila), (brillo, 255, 255))
    
img_rgb = img.convert('RGB')
img_rgb.save("mandelbrot-clase2.png")

print("DONE")