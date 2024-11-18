# Python Car Game

The game is a puzzle game where the player must maneuver vehicles on a grid to create a clear path for a specific vehicle (usually "A") to exit the grid. The game involves the following:

## Key Elements

**Grid Representation:**
- A rectangular grid, typically shown with characters representing different vehicles.
- Each vehicle occupies one or more grid cells.
- The grid boundaries and obstacles prevent free movement.

**Objective:**

Move vehicles horizontally or vertically to create an unobstructed path for the target vehicle ("A") to exit.

**Constraints:**

- Vehicles can only move in specific directions (horizontally or vertically, depending on their orientation).
- Limited moves or an optimal solution might be tracked for added challenge.

**Game Inputs:**

- Players specify moves using a simple syntax or key inputs (e.g., "Move B left" or "B-1L").
- Each move shifts a vehicle by a specific number of cells in a valid direction.

**Winning Condition:**

The player wins when the target vehicle exits the grid.

## Development Goals

- User Interaction: Players input moves and receive feedback (valid/invalid move, game progress).
- File-based Input: The game can load initial grids from a text file, making it customizable.
- Replayability: Different starting grids and configurations allow for varied levels of difficulty.

## How To Play the Game

### 1. Clone the Project

We start by cloning the repository to your pc and then navigating to the project following those commands 
```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Setting Up the Virtual Enviroment

Then we have to create a vertual enviroment for the project with this command

```bash
python -m venv venv
```

Activate the virtual enviroment using the following command 

**(Linux/MacOS)**
```bash
source venv/bin/activate
```

**(Windows)**
```bash
venv\Scripts\activate
```
Finally, we have to install the dependencies which are defined in the "requirements.txt" file

```bash
pip install -r requirements.txt
```

### 3. Launch the Game

To launch the game run the following command

```bash
python main.py "game_file.txt"
```