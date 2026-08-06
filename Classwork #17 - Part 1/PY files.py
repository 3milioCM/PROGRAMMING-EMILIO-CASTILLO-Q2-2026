import os
import pygame

# Find config.txt in the same folder as this script
script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, 'config.txt')

config = {}
with open(config_path, 'r') as file:
    for line in file:
        parameter, value = line.strip().split('=')
        if ',' in value:
            config[parameter] = tuple(int(c.strip()) for c in value.split(','))
        elif '.' in value:
            config[parameter] = float(value)
        else:
            config[parameter] = int(value)

vanishing_point = (config['width'] * 0.5, config['height'] * 0.25)

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
    height      = surface.get_height()
    spacing     = height / (horizontal_lines + 1)
    
    for i in range(1, horizontal_lines + 1):
        y_positions.append(i * spacing)  # Fixed: changed 1 * spacing to i * spacing
        
    return y_positions
def find_intersection(line_1, line_2):
    """
    Find the intersections between two lines
    """
    start_point_line_1, end_point_line_1 = line_1
    start_point_line_2, end_point_line_2 = line_2
 
    x1, y1 = start_point_line_1
    x2, y2 = end_point_line_1
    x3, y3 = start_point_line_2
    x4, y4 = end_point_line_2
 
    denominator     = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    common_factor_a = x1 * y2 - y1 * x2
    common_factor_b = x3 * y4 - y3 * x4
 
    if denominator == 0:
        return None
 
    intersection_x = (common_factor_a * (x3 - x4) - (x1 - x2) * common_factor_b) / denominator
    intersection_y = (common_factor_a * (y3 - y4) - (y1 - y2) * common_factor_b) / denominator
 
    return (intersection_x, intersection_y)
def draw_vertical_lines(surface, x_positions, color, width=2):
    height = surface.get_height()

    for x in x_positions: 
        pygame.draw.line(surface, color, (x, 0), (x, height), width)

def draw_perspective_vertical_lines(surface, x_positions, vanishing_point, color, width=2):
    height = surface.get_height()

    for x in x_positions:
        end_point = (x, height)
        pygame.draw.line(surface, color, vanishing_point, end_point, width)
def draw_perspective_horizontal_lines(surface, x_positions, y_positions, vanishing_point, color, width=2):
    height = surface.get_height()
    
    for y in y_positions:
        if y >= vanishing_point[1]:  # Only draw lines below the vanishing point
            diagonal_1 = (vanishing_point, (x_positions[0], height))
            diagonal_2 = (vanishing_point, (x_positions[-1], height))
            h_line     = ((x_positions[0], y), (x_positions[-1], y))
            
            intersection_1 = find_intersection(diagonal_1, h_line)
            intersection_2 = find_intersection(diagonal_2, h_line)
            
            pygame.draw.line(surface, color, intersection_1, intersection_2, width)


def draw_horizontal_lines(surface, x_positions, y_positions, color, width=2):
    for y in y_positions:
        start_point = (x_positions[0], y)
        end_point   = (x_positions[-1], y)
        pygame.draw.line(surface, color, start_point, end_point, width)

pygame.init()
screen = pygame.display.set_mode((config['width'], config['height']))

# MAIN LOOP
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
    # draw_vertical_lines(screen, x_positions, config['line_color'])
    # draw_horizontal_lines(screen, x_positions, y_positions, config['line_color'])
    draw_perspective_vertical_lines(screen, x_positions, vanishing_point, config['line_color'])
    draw_perspective_horizontal_lines(screen, x_positions, y_positions, vanishing_point, config['line_color'])
    pygame.display.flip()

pygame.quit()  