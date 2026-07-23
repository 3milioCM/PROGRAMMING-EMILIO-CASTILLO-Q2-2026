import random
import stddraw
from color import Color

def draw_bars(numbers, selected=()):
    stddraw.clear()
    n = len(numbers)
    # El ancho de la barra se calcula para que todas quepan en el eje X (de 0 a n)
    bar_width = n / n  # Esto es 1.0, pero mantenemos tu lógica adaptada
    
    for i, number in enumerate(numbers):
        x = i * bar_width + bar_width / 2
        color = Color(255, 90, 90) if i in selected else Color(70, 130, 220)
        stddraw.setPenColor(color)
        stddraw.filledRectangle(x - bar_width / 2, 0, bar_width * 0.9, number)
    stddraw.show(100)

def bubble_sort_animated(numbers):
    n = len(numbers)
    stddraw.setXscale(-0.1, n)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    
    for sweep in range(n):
        swapped = False
        for pair in range(0, n - 1 - sweep):
            draw_bars(numbers, selected=(pair, pair+1))
            if numbers[pair] > numbers[pair+1]:
                numbers[pair], numbers[pair + 1] = numbers[pair+1], numbers[pair]
                swapped = True
            draw_bars(numbers, selected=(pair, pair+1))
            
        if not swapped:
            break
        
    draw_bars(numbers)

def insertion_sort_animated(numbers):
    n = len(numbers)
    stddraw.setXscale(-0.1, n)
    stddraw.setYscale(-0.5, max(numbers) + 1)

    for i in range(1, n):
        key = numbers[i]
        j = i - 1
        
        # Resaltamos el elemento que vamos a insertar
        draw_bars(numbers, selected=(i,))
        
        while j >= 0 and numbers[j] > key:
            draw_bars(numbers, selected=(j, j+1))
            numbers[j + 1] = numbers[j]
            j -= 1
            draw_bars(numbers, selected=(j+1, j+2))
            
        numbers[j + 1] = key
        # Resaltamos dónde quedó insertado finalmente
        draw_bars(numbers, selected=(j+1,))

    draw_bars(numbers)

def selection_sort_animated(numbers):
    n = len(numbers)
    stddraw.setXscale(-0.1, n)
    stddraw.setYscale(-0.5, max(numbers) + 1)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            draw_bars(numbers, selected=(min_index, j))
            if numbers[j] < numbers[min_index]:
                min_index = j
                
        if min_index != i:
            draw_bars(numbers, selected=(i, min_index))
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
            draw_bars(numbers, selected=(i, min_index))

    draw_bars(numbers)


if __name__ == "__main__":
    # Prueba con Bubble Sort
    # arr1 = [random.randint(0, 100) for _ in range(10)]
    # print(f"Before bubble sort: {arr1}")
    # bubble_sort_animated(arr1)
    # print(f"After bubble sort: {arr1}\n")
    

    # Prueba con Insertion Sort

    # arr2 = [random.randint(0, 100) for _ in range(10)]
    # print(f"Before insertion sort: {arr2}")
    # insertion_sort_animated(arr2)
    # print(f"After insertion sort: {arr2}\n")

    # Prueba con Selection Sort

    arr3 = [random.randint(0, 100) for _ in range(10)]
    print(f"Before selection sort: {arr3}")
    selection_sort_animated(arr3)
    print(f"After selection sort: {arr3}")
    
    # Mantiene la ventana abierta al final
    stddraw.show() 

