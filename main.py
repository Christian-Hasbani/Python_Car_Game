from file_parser import parse_game  # Import parse_game from file_parser.py
from display import get_game_str  # Import get_game_str from display.py
from move_car import move_car  # Import move_car from move_car.py

def main():
    # Path to the game configuration file
    game_file_path = "example_game.txt"

    # Step 1: Parse the game configuration file
    game = parse_game(game_file_path)

    # Step 2: Initialize game variables
    current_move_number = 0
    max_moves = game["max_moves"]

    print("Welcome to ULBloqué!")
    print("The goal is to free car 'A' by moving other cars blocking its path.")
    print("Use 'UP', 'DOWN', 'LEFT', or 'RIGHT' to move cars.")
    print("Type 'exit' to quit the game.\n")

    while current_move_number < max_moves:
        # Step 3: Display the current game state
        print(get_game_str(game, current_move_number))

        # Step 4: Prompt user to select a car and direction
        car_letter = input("Select a car to move (e.g., A, B, C): ").strip().upper()
        if car_letter == "EXIT":
            print("You exited the game. Goodbye!")
            break

        try:
            car_index = ord(car_letter) - ord('A')  # Convert letter to index
            if car_index < 0 or car_index >= len(game["cars"]):
                print("Invalid car selection. Try again.")
                continue

            direction = input("Enter the direction to move (UP, DOWN, LEFT, RIGHT): ").strip().upper()
            if direction not in ["UP", "DOWN", "LEFT", "RIGHT"]:
                print("Invalid direction. Try again.")
                continue

            # Step 5: Attempt to move the car
            if move_car(game, car_index, direction):
                print(f"Moved car {car_letter} {direction.lower()}.")
                current_move_number += 1
            else:
                print(f"Cannot move car {car_letter} {direction.lower()}. Try again.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

    # Step 6: Game over (out of moves or victory check would go here)
    if current_move_number >= max_moves:
        print("You've used all your moves. Game over!")
    else:
        print("Congratulations, you've freed car 'A'!")

if __name__ == "__main__":
    main()
