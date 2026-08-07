import random
from grid import draw_grid_sector, draw_perspective_grid_sector

def generate_path(rows, columns, start_column=None, chance=0.4):
    if start_column is None:
        start_column = columns // 2

    current_column = max(0, min(start_column, columns - 1))
    world_row = 0
    path_data = [(world_row, [current_column])]

    can_turn = True
    while len(path_data) < rows:
        if can_turn and random.random() < chance:
            valid_directions = [
                d for d in (-1, 1)
                if 0 <= current_column + d < columns
            ]
            if valid_directions:
                direction  = random.choice(valid_directions)
                new_column = current_column + direction
                world_row += 1
                path_data.append((world_row, [current_column, new_column]))
                current_column = new_column
                can_turn = False
                continue

        world_row += 1
        path_data.append((world_row, [current_column]))
        can_turn = True

    return path_data

def advance_path(path_data, columns, chance=0.4):
    path_data.pop(0)

    last_row, last_columns = path_data[-1]
    current_column = last_columns[-1]
    can_turn = (len(last_columns) == 1)

    if can_turn and random.random() < chance:
        valid_directions = [
            d for d in (-1, 1)
            if 0 <= current_column + d < columns
        ]
        if valid_directions:
            direction = random.choice(valid_directions)
            candidate = current_column + direction
            new_row   = last_row + 1
            path_data.append((new_row, [current_column, candidate]))
            return

    new_row = last_row + 1
    path_data.append((new_row, [current_column]))

def get_columns_at_local_row(path_data, local_row):
    reversed_data = path_data[::-1]
    if 0 <= local_row < len(reversed_data):
        _, columns = reversed_data[local_row]
        return columns
    return None

def draw_path(surface, path_data, x_positions, y_positions, color):
    max_rows = len(y_positions) - 1
    max_cols = len(x_positions) - 1

    for local_row, (_, columns) in enumerate(path_data):
        if local_row >= max_rows:
            break

        valid_columns = [c for c in columns if 0 <= c < max_cols]
        if valid_columns:
            draw_grid_sector(
                surface=surface,
                columns=valid_columns,
                row=local_row,
                x_positions=x_positions,
                y_positions=y_positions,
                color=color
            )

def draw_perspective_path(surface, path_data, x_positions, y_positions, vanishing_point, color):
    max_rows = len(y_positions) - 1
    max_cols = len(x_positions) - 1

    for local_row, (_, columns) in enumerate(path_data):
        if local_row >= max_rows:
            break

        if y_positions[local_row] <= vanishing_point[1]:
            continue

        valid_columns = [c for c in columns if 0 <= c < max_cols]
        if valid_columns:
            draw_perspective_grid_sector(
                surface=surface,
                columns=valid_columns,
                row=local_row,
                x_positions=x_positions,
                y_positions=y_positions,
                vanishing_point=vanishing_point,
                color=color
            ) 