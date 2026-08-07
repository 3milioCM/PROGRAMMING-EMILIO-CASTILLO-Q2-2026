import pygame
from geometry import find_row_at_y, x_on_diagonal
from path import get_columns_at_local_row

def draw_ship(surface, position, size, color):
    x, y       = position
    half_width = size[0] / 2
    height     = size[1]

    tip   = (x, y - height)
    left  = (x - half_width, y)
    right = (x + half_width, y)

    pygame.draw.polygon(surface, color, [tip, left, right])

def get_ship_vertices(position, size):
    x, y       = position
    half_width = size[0] / 2
    height     = size[1]

    tip   = (x, y - height)
    left  = (x - half_width, y)
    right = (x + half_width, y)

    return [tip, left, right]

def check_collision(ship_vertices, path_data, x_positions, y_curved, vanishing_point, surface_height):
    for vx, vy in ship_vertices:
        local_row = find_row_at_y(y_curved, vy)
        if local_row is None:
            continue

        columns = get_columns_at_local_row(path_data, local_row)
        if not columns:
            return True

        left_x  = x_on_diagonal(vanishing_point, x_positions[min(columns)],     surface_height, vy)
        right_x = x_on_diagonal(vanishing_point, x_positions[max(columns) + 1], surface_height, vy)

        if not (left_x <= vx <= right_x):
            return True

    return False 