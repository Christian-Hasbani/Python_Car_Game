def parse_game(game_file_path: str) -> dict:
    """
    Parse the game configuration file to initialize the game state.

    Args:
        game_file_path (str): Path to the game configuration file.

    Returns:
        dict: A dictionary representing the initial game state.
    """
    game = {
        "width": 0,
        "height": 0,
        "cars": [],
        "max_moves": 0
    }

    try:
        with open(game_file_path, 'r') as file:
            lines = file.readlines()

        # Extract the parking grid
        grid_lines = [line.strip() for line in lines if '|' in line]

        # Determine grid dimensions
        game["height"] = len(grid_lines)
        game["width"] = len(grid_lines[0]) - 2  # Exclude border symbols (|)

        # Parse cars and spaces
        car_positions = {}
        for y, line in enumerate(grid_lines):
            for x, char in enumerate(line[1:-1]):  # Exclude vertical borders
                if char.isalpha():  # Identify a car
                    if char not in car_positions:
                        car_positions[char] = {"coords": [], "orientation": ""}
                    car_positions[char]["coords"].append((x, y))

        # Determine car orientation and size
        for char, data in car_positions.items():
            coords = data["coords"]
            if len(coords) > 1:  # Only multi-cell objects are cars
                if coords[0][0] == coords[1][0]:  # Same x -> Vertical
                    orientation = 'v'
                else:  # Same y -> Horizontal
                    orientation = 'h'
                game["cars"].append({
                    "position": coords[0],  # Top-left or first cell
                    "orientation": orientation,
                    "size": len(coords)  # Total number of cells occupied
                })

        # Extract maximum moves
        game["max_moves"] = int(lines[-1].strip())

    except FileNotFoundError:
        print(f"Error: File '{game_file_path}' not found.")
        exit(1)
    except Exception as e:
        print(f"Error parsing file: {e}")
        exit(1)

    return game
