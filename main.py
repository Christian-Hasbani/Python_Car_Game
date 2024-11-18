import sys
from getkey import getkey,keys

# Fonction 1 : Parsing du fichier
def parse_game(game_file_path: str) -> dict:
    with open(game_file_path, 'r') as file:
        lines = file.readlines()

    width = len(lines[1].strip()) - 2
    height = len(lines) - 3
    exit = [0, 0]

    cars = {}
    for y, line in enumerate(lines[1:-2]):
        for x, char in enumerate(line.strip()[1:-1]):
            if char.isalpha():
                if char not in cars:
                    cars[char] = []
                cars[char].append((x, y))

        if line.strip()[-1] == '.':
            exit = [len(line.strip()) - 2, y]

    parsed_cars = []
    for char in sorted(cars.keys()):  # Sort alphabetically by car name
        positions = sorted(cars[char])
        orientation = 'h' if len(positions) > 1 and positions[0][1] == positions[1][1] else 'v'
        origin = positions[0]
        size = len(positions)
        parsed_cars.append([char, origin, orientation, size])

    max_moves = int(lines[-1].strip())

    return {
        'width': width,
        'height': height,
        'cars': parsed_cars,
        'max_moves': max_moves,
        'exit': exit
    }



# Fonction 2 : Affichage du jeu
def get_game_str(game: dict, current_move_number: int) -> str:
    grid = [['.'] * game['width'] for _ in range(game['height'])]
    colors = ['\u001b[47;30m', '\u001b[41m', '\u001b[42m', '\u001b[43m', '\u001b[44m', '\u001b[45m', '\u001b[46m']

    for i, car in enumerate(game['cars']):
        color = colors[i % len(colors)]
        name, origin, orientation, size = car
        for j in range(size):
            x, y = origin
            if orientation == 'h':
                grid[y][x + j] = f"{color}{name}\u001b[0m"
            else:
                grid[y + j][x] = f"{color}{name}\u001b[0m"
    
    border = '+' + '-' * game['width'] + '+\n'
    grid_str = border
    for index, row in enumerate(grid):
        if(index == game['exit'][1] and game['exit'][0] == 0):
            grid_str += '.' + ''.join(row) + '|\n'
        elif(index == game['exit'][1] and game['exit'][0] == 6):
            grid_str += '|' + ''.join(row) + '.\n'
        else:
            grid_str += '|' + ''.join(row) + '|\n'

    grid_str += border
    grid_str += f"Moves: {current_move_number}/{game['max_moves']}"
    return grid_str

# Fonction 3 : Déplacer une voiture
def move_car(game: dict, car_index: int, direction: str) -> bool:
    # Fetch the car
    car = game['cars'][car_index]
    name, origin, orientation, size = car
    print(f"Attempting to move car '{name}' at index {car_index} with orientation '{orientation}'")

    x, y = origin
    dx, dy = 0, 0

    # Map direction to dx, dy
    if direction == keys.UP:
        dy = -1
    elif direction == keys.DOWN:
        dy = 1
    elif direction == keys.LEFT:
        dx = -1  # Horizontal movement, moving left
    elif direction == keys.RIGHT:
        dx = 1   # Horizontal movement, moving right
    else:
        print("Invalid direction input")
        return False

    # Validate move against orientation
    if (orientation == 'h' and dy != 0) or (orientation == 'v' and dx != 0):
        print(f"Invalid move for car '{name}': orientation={orientation}, dx={dx}, dy={dy}")
        return False

    # Check for collisions and boundaries for each part of the car
    if orientation == 'h':
        # For horizontal cars, we need to check all parts of the car (each x position)
        for i in range(size):
            new_x = x + dx * i  # Calculate new x for each part of the car
            new_y = y            # y stays the same for horizontal movement

            print(f"Checking position: ({new_x}, {new_y})")
            
            # Check if the new position is out of bounds
            if new_x < -1 or new_x >= game['width'] or new_y < -1 or new_y >= game['height']:
                print(f"Move out of bounds for car '{name}': ({new_x}, {new_y})")
                return False

            # Check for collisions with other cars
            for other_car in game['cars']:
                if other_car == car:
                    continue  # Skip collision check for the same car

                ox, oy = other_car[1]
                o_size = other_car[3]
                occupied_positions = []

                if other_car[2] == 'h':
                    # Get occupied positions for horizontal cars
                    occupied_positions = [(ox + i, oy) for i in range(o_size)]
                else:
                    # Get occupied positions for vertical cars
                    occupied_positions = [(ox, oy + i) for i in range(o_size)]

                if (new_x, new_y) in occupied_positions:
                    print(f"Collision detected with car '{other_car[0]}' at ({new_x}, {new_y})")
                    return False
    elif orientation == 'v':
        # Check vertical movement, similar logic but with y and dx
        for i in range(size):
            new_x = x            # x stays the same for vertical movement
            new_y = y + dy * i   # Calculate new y for each part of the car

            print(f"Checking position: ({new_x}, {new_y})")
            
            if new_x < -1 or new_x >= game['width'] or new_y < -1 or new_y >= game['height']:
                print(f"Move out of bounds for car '{name}': ({new_x}, {new_y})")
                return False

            for other_car in game['cars']:
                if other_car == car:
                    continue

                ox, oy = other_car[1]
                o_size = other_car[3]
                occupied_positions = []

                if other_car[2] == 'h':
                    occupied_positions = [(ox + i, oy) for i in range(o_size)]
                else:
                    occupied_positions = [(ox, oy + i) for i in range(o_size)]

                if (new_x, new_y) in occupied_positions:
                    print(f"Collision detected with car '{other_car[0]}' at ({new_x}, {new_y})")
                    return False

    # Update car position
    car[1] = (x + dx, y + dy)
    print(f"Car '{name}' moved to new origin: {car[1]}")
    return True


# Fonction 4 : Vérification de la victoire
def is_win(game: dict) -> bool:
    car_a = game['cars'][0]
    x, y = car_a[0]
    return x + car_a[2] == game['width']

# Fonction 5 : Démarrage/Boucle de la partie
def play_game(game: dict) -> int:
    current_move = 0
    while current_move < game['max_moves']:
        print(get_game_str(game, current_move))
        try:
            car_choice = getkey().upper()
            if car_choice == keys.ESCAPE:
                return 2
            else:
                print(f"You have chosen the {car_choice} car")
            car_index = ord(car_choice) - ord('A')
            if car_index < 0 or car_index >= len(game['cars']):
                continue
            direction = getkey().upper()
            if direction == keys.ESCAPE:
                return 2
            if move_car(game, car_index, direction):
                current_move += 1
            if is_win(game):
                print(get_game_str(game, current_move))
                return 0
        except Exception:
            continue
    return 1

# __main__ : Chargement et lancement
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python game.py <game_file_path>")
        sys.exit(1)
    game_file_path = sys.argv[1]
    game = parse_game(game_file_path)
    result = play_game(game)
    if result == 0:
        print("Congratulations! You've won!")
    elif result == 1:
        print("Game over. You've run out of moves.")
    else:
        print("Game aborted.")
