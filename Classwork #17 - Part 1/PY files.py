import os
import pygame


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(BASE_DIR, 'config.txt')


config = {}
with open(config_path, 'r', encoding='utf-8-sig') as file:
    for line in file:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        if '=' in line:
            parameter, value = line.split('=', 1)
            parameter = parameter.strip()
            value = value.strip()
            
            if ',' in value:
                config[parameter] = tuple(int(c.strip()) for c in value.split(','))
            elif '.' in value:
                config[parameter] = float(value)
            else:
                config[parameter] = int(value)


def calculate_x_positions(surface, vertical_lines, space):
    x_positions  = []
    width        = surface.get_width()
    spacing      = space * width
    central_line = width / 2
    offset       = -int(vertical_lines / 2)

    for _ in range(vertical_lines):
        x_positions.append(central_line + offset * spacing)
        offset += 1

    return x_positions

def calculate_y_positions(surface, horizontal_lines):
    y_positions = []
    height = surface.get_height()
    spacing = height / (horizontal_lines + 1)

    for i in range(1, horizontal_lines + 1):
        y_positions.append(i * spacing)

    return y_positions

def draw_vertical_lines(surface, x_positions, color, width=2):
    height = surface.get_height()
    for x in x_positions:
        pygame.draw.line(surface, color, (x, 0), (x, height), width)

def draw_horizontal_lines(surface, x_positions, y_positions, color, width=2):
    if not x_positions:
        return
    x_start = x_positions[0]
    x_end = x_positions[-1]

    for y in y_positions:
        pygame.draw.line(surface, color, (x_start, y), (x_end, y), width)

# 4. Inicialización e interfaz gráfica
pygame.init()
screen = pygame.display.set_mode((config['width'], config['height']))

# MAIN LOOP / Configuración de posiciones
x_positions = calculate_x_positions(
    surface=screen,
    vertical_lines=config['vertical_lines'],
    space=config['space']
)
print(x_positions)   

y_positions = calculate_y_positions(
    surface=screen,
    horizontal_lines=config['horizontal_lines']
)
print(y_positions)   


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(config['bg_color'])
    draw_vertical_lines(screen, x_positions, config['line_color'])
    draw_horizontal_lines(screen, x_positions, y_positions, config['line_color'])
    pygame.display.flip()

pygame.quit() 