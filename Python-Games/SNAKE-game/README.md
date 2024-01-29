Python Turtle Snake Game

Overview:

    -This is a Python implementation of the classic Snake game. The player controls a snake, trying to eat food to grow longer while avoiding hitting the game window boundaries or itself. The game is built using the Python turtle module for graphics.

Modules:

    -MAIN.py: The main game script.
    -snake.py: Contains the Snake class, managing the snake's behavior and appearance.
    -food.py: Defines the Food class, which randomly places food on the screen.
    -scoreboard.py: Manages the game's scoreboard.

Requirements

    -Python 3.x
    -Turtle Graphics Library (usually included in standard Python installations)

Gameplay

    -Use the arrow keys to control the snake's direction.
    -Eat food to grow the snake and earn points.
    -Avoid colliding with the game window edges or the snake's own body.
    -The game ends when the snake collides with the window boundary or itself.

How to Run

    -Ensure all files (MAIN.py, snake.py, food.py, scoreboard.py) are in the same directory.
    -Run MAIN.py in a Python environment:

Customization

    -Change the snake or food color by modifying the color method in the Snake and Food classes.
    -Adjust the game speed by changing the time.sleep() value in MAIN.py.
