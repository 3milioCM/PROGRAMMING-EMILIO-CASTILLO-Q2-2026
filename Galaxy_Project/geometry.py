def calculate_x_positions(surface, vertical_lines, space):
    x_positions = []
    width = surface.get_width()
    spacing = space * width
    central_line = width / 2
    offset = -int(vertical_lines / 2)

    for i in range(vertical_lines):
        x_positions.append(central_line + (offset * spacing))
        offset += 1

    return x_positions

def calculate_y_positions(surface, horizontal_lines):
    y_positions = []
    height = surface.get_height()
    spacing = height / (horizontal_lines + 1)

    for i in range(1, horizontal_lines + 2):  # Fila extra para recorte en perspectiva
        y_positions.append(i * spacing)

    return y_positions

def find_intersection(line_1, line_2):
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

def non_linear_spacing(surface, y_positions, vanishing_point, power=2.0):
    height           = surface.get_height()
    v_y              = vanishing_point[1]
    available_height = height - v_y
    y_curved         = []

    for y in y_positions:
        t     = (y - v_y) / available_height
        sign  = 1 if t >= 0 else -1
        new_y = v_y + available_height * sign * (abs(t) ** power)
        y_curved.append(new_y)

    return y_curved

def x_on_diagonal(vanishing_point, x_at_bottom, surface_height, y):
    vx, vy = vanishing_point
    if surface_height == vy:
        return vx
    t = (y - vy) / (surface_height - vy)
    return vx + t * (x_at_bottom - vx)

def find_row_at_y(y_curved, y):
    for i in range(len(y_curved) - 1):
        if y_curved[i] <= y <= y_curved[i + 1]:
            return i
    return None 