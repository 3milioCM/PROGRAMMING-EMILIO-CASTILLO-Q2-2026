import pygame
from geometry import find_intersection

def draw_vertical_lines(surface, x_positions, color, width=2):
    height = surface.get_height()
    for x in x_positions:
        pygame.draw.line(surface, color, (x, 0), (x, height), width)

def draw_perspective_vertical_lines(surface, x_positions, vanishing_point, color, width=2):
    height = surface.get_height()
    for x in x_positions:
        pygame.draw.line(surface, color, vanishing_point, (x, height), width)

def draw_horizontal_lines(surface, x_positions, y_positions, color, width=2):
    for y in y_positions:
        start_point = (x_positions[0], y)
        end_point   = (x_positions[-1], y)
        pygame.draw.line(surface, color, start_point, end_point, width)

def draw_perspective_horizontal_lines(surface, x_positions, y_positions, vanishing_point, color, width=2):
    height      = surface.get_height()
    start_point = vanishing_point

    diagonal_1 = (start_point, (x_positions[0], height))
    diagonal_2 = (start_point, (x_positions[-1], height))

    for y in y_positions:
        if y > vanishing_point[1]:
            point_1 = (x_positions[0], y)
            point_2 = (x_positions[-1], y)

            h_line = (point_1, point_2)

            intersection_1 = find_intersection(diagonal_1, h_line)
            intersection_2 = find_intersection(diagonal_2, h_line)

            if intersection_1 and intersection_2:
                pygame.draw.line(surface, color, intersection_1, intersection_2, width)

def draw_grid_sector(surface, columns, row, x_positions, y_positions, color):
    left_col  = min(columns)
    right_col = max(columns)

    x_left  = x_positions[left_col]
    x_right = x_positions[right_col + 1]

    y_top    = y_positions[row]
    y_bottom = y_positions[row + 1]

    pygame.draw.polygon(surface, color, [
        (x_left, y_bottom), (x_right, y_bottom),
        (x_right, y_top),   (x_left, y_top)
    ])

def draw_perspective_grid_sector(surface, columns, row, x_positions, y_positions, vanishing_point, color):
    height    = surface.get_height()
    left_col  = min(columns)
    right_col = max(columns)

    diagonal_left  = (vanishing_point, (x_positions[left_col], height))
    diagonal_right = (vanishing_point, (x_positions[right_col + 1], height))

    y_top    = y_positions[row]
    y_bottom = y_positions[row + 1]

    h_line_top    = ((x_positions[0], y_top), (x_positions[-1], y_top))
    h_line_bottom = ((x_positions[0], y_bottom), (x_positions[-1], y_bottom))

    tl_point = find_intersection(diagonal_left,  h_line_top)
    tr_point = find_intersection(diagonal_right, h_line_top)
    br_point = find_intersection(diagonal_right, h_line_bottom)
    bl_point = find_intersection(diagonal_left,  h_line_bottom)

    if None in (tl_point, tr_point, br_point, bl_point):
        return

    pygame.draw.polygon(surface, color, [bl_point, br_point, tr_point, tl_point]) 