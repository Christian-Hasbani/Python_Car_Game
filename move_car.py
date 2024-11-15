def move_car(game: dict, car_index: int, direction: str) -> bool:
    """
    Move a car in the specified direction if the movement is valid.

    Args:
        game (dict): The current game state dictionary.
        car_index (int): Index of the car to move (0 for A, 1 for B, etc.).
        direction (str): The direction to move ('UP', 'DOWN', 'LEFT', 'RIGHT').

    Returns:
        bool: True if the movement was successful, False otherwise.
    """
    # Retrieve the car details
    car = game["cars"][car_index]
    x, y = car["position"]
    orientation = car["orientation"]
    size = car["size"]

    # Calculate the new position based on the direction
    dx, dy = 0, 0
    if direction == "UP":
        dy = -1
    elif direction == "DOWN":
        dy = 1
    elif direction == "LEFT":
        dx = -1
    elif direction == "RIGHT":
        dx = 1
    else:
        return False  # Invalid direction

    # Ensure the movement matches the car's orientation
    if (orientation == 'h' and dy != 0) or (orientation == 'v' and dx != 0):
        return False  # Horizontal cars can't move vertically, and vice versa

    # Check if the new position is valid
    for i in range(size):
        # Calculate new coordinates for each segment of the car
        if orientation == 'h':
            new_x = x + dx + i
            new_y = y + dy
        elif orientation == 'v':
            new_x = x + dx
            new_y = y + dy + i

        # Ensure new position is within bounds
        if not (0 <= new_x < game["width"] and 0 <= new_y < game["height"]):
            return False

        # Check for collision with other cars
        for other_car in game["cars"]:
            if other_car == car:  # Skip self
                continue
            ox, oy = other_car["position"]
            osize = other_car["size"]
            oorientation = other_car["orientation"]

            for j in range(osize):
                if oorientation == 'h' and (ox + j, oy) == (new_x, new_y):
                    return False
                elif oorientation == 'v' and (ox, oy + j) == (new_x, new_y):
                    return False

    # Update the car's position
    car["position"] = (x + dx, y + dy)
    return True
