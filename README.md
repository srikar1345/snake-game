# Snake Game

A classic Snake game built with Python's turtle graphics module.

## Features
- Move the snake using W (up), S (down), A (left), D (right)
- Eat the food to grow longer
- Score is displayed at the top
- Game over message with final score

## Libraries Used

- **turtle**: Used for all game graphics, drawing the snake, food, and scoreboard, and handling keyboard input.
- **time**: Used to control the speed of the game loop (with `time.sleep`).
- **random**: Used to randomly place the food on the screen after it is eaten.

## How to Run
1. Make sure you have Python installed (version 3.x).
2. Install the `turtle` module if needed (usually included with Python).
3. Run the game:
   ```bash
   python wer.py
   ```
4. Control the snake using your keyboard:
   - W: Up
   - S: Down
   - A: Left
   - D: Right

## Screenshot

![Snake Game Screenshot](game%20photo.jpg)

## Files
- `wer.py` - Main game loop and logic
- `snake.py` - Snake class and movement
- `food.py` - Food class
- `scoreboard.py` - Scoreboard display

Enjoy playing!
