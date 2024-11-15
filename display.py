def get_game_str(game: dict, current_move_number: int) -> str:
    """
    Generate a string representation of the current game state.

    Args:
        game (dict): The current game state dictionary.
        current_move_number (int): The number of moves used so far.

    Returns:
        str: A string representation of the game state.
    """
    width = game["width"]
    height = game["height"]
    cars = game["cars"]
    max_moves = game["max_moves"]

    # Create a blank grid
    grid = [["." for _ in range(width)] for _ in range(height)]

    # Place the cars on the grid
    for index, car in enumerate(cars):
        x, y = car["position"]
        orientation = car["orientation"]
        size = car["size"]

        # Assign a letter for each car (A, B, C, ...)
        car_letter = chr(ord('A') + index)

        # Fill the car's position on the grid
        for i in range(size):
            if orientation == "h":
                grid[y][x + i] = car_letter
            elif orientation == "v":
                grid[y + i][x] = car_letter

    # Build the display string
    output = []

    # Top border
    output.append("+" + "-" * width + "+")

    # Grid rows
    for row in grid:
        output.append("|" + "".join(row) + "|")

    # Bottom border
    output.append("+" + "-" * width + "+")

    # Display moves
    moves_used = current_move_number
    moves_remaining = max_moves - current_move_number
    output.append(f"Moves used: {moves_used}")
    output.append(f"Moves remaining: {moves_remaining}")

    # Join all parts into a single string
    return "\n".join(output)
