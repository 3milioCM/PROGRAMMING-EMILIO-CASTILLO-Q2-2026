import pygame
from config import load_config
from geometry import calculate_x_positions, calculate_y_positions, non_linear_spacing
from grid import draw_perspective_vertical_lines, draw_perspective_horizontal_lines
from path import generate_path, advance_path, draw_perspective_path
from ship import draw_ship, get_ship_vertices, check_collision

# INITIALIZATION
config = load_config('config.txt')

pygame.init()
screen     = pygame.display.set_mode((config['width'], config['height']))
clock      = pygame.time.Clock()
target_fps = 60.0

vanishing_point = (config['width'] * 0.5, config['height'] * 0.25)

speed         = config['speed']
scroll_offset = 0.0
line_spacing  = config['height'] / (config['horizontal_lines'] + 1)

# Horizontal Controls Setup
x_offset  = 0.0
x_speed   = 300.0
x_spacing = config['space'] * config['width']

scroll_accumulator = 0.0

# Ship Setup
ship_size     = (35, 25)
ship_position = (config['width'] / 2, config['height'] * 0.85)

# Calculate base grid points
x_positions = calculate_x_positions(
    surface=screen,
    vertical_lines=config['vertical_lines'],
    space=config['space']
)

y_positions = calculate_y_positions(
    surface=screen,
    horizontal_lines=config['horizontal_lines']
)

path_data = generate_path(
    rows=len(y_positions) - 1,
    columns=len(x_positions) - 1,
    start_column=(len(x_positions) - 1) // 2,
    chance=0.35
)

max_x_offset = (len(x_positions) / 2.75) * x_spacing

# MAIN LOOP
running = True
while running:
    dt = min(clock.tick(target_fps) / 1000.0, 0.05)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(config['bg_color'])
    
    # HORIZONTAL SCROLLING & SHIP STEERING
    # Se invirtió la dirección del desplazamiento (+ en LEFT, - en RIGHT) 
    # para que la nave apunte e ir al lado correcto relativo a la grilla.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_offset += x_speed * dt
    elif keys[pygame.K_RIGHT]:
        x_offset -= x_speed * dt

    x_offset          = max(-max_x_offset, min(x_offset, max_x_offset))
    animated_x_points = [x + x_offset for x in x_positions]
    
    # VERTICAL SCROLLING
    frame_movement      = speed * dt
    scroll_accumulator += frame_movement
    scroll_offset       = (scroll_offset + frame_movement) % line_spacing
    
    if scroll_accumulator >= line_spacing:
        scroll_accumulator -= line_spacing
        advance_path(
            path_data=path_data,
            columns=len(x_positions) - 1
        )

    animated_y_points = [y + scroll_offset for y in y_positions]
    y_curved          = non_linear_spacing(screen, animated_y_points, vanishing_point)
    
    # RENDER PERSPECTIVE GRID & PATH
    draw_perspective_vertical_lines(screen, animated_x_points, vanishing_point, config['line_color'])
    draw_perspective_horizontal_lines(screen, animated_x_points, y_curved, vanishing_point, config['line_color'], width=2)
    draw_perspective_path(screen, path_data[::-1], animated_x_points, y_curved, vanishing_point, config['line_color'])
    
    # RENDER SHIP & CHECK COLLISION
    draw_ship(screen, ship_position, ship_size, config['ship_color'])
    
    ship_vertices = get_ship_vertices(ship_position, ship_size)
    collided      = check_collision(ship_vertices, path_data, animated_x_points, y_curved, vanishing_point, surface_height=config['height'])

    if collided:
        print("COLLISION")
    
    pygame.display.flip()

pygame.quit() 