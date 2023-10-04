# Pong Game

This is a simple implementation of the classic Pong game using Python's Turtle graphics library. The game features two paddles, one on the left and one on the right, and a bouncing ball. The objective is to prevent the ball from passing your paddle while trying to score points by getting the ball past your opponent's paddle.

## Prerequisites

To run the Pong game, you'll need Python installed on your system. Make sure you have Python installed, and you're good to go!

## Getting Started

1. Clone or download the repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where you saved the game files.

3. Run the game by executing the following command:
   
   ```
   python main.py
   ```

4. Use the following controls to play the game:
   - **Right Paddle** (Player on the right):
     - Move Up: Up Arrow Key
     - Move Down: Down Arrow Key
   - **Left Paddle** (Player on the left):
     - Move Up: 'w' Key
     - Move Down: 's' Key

5. The game will continue until one player scores a certain number of points. You can adjust the winning score limit in the code if needed.

6. Enjoy the game and have fun!

## Game Features

- Two-player game with customizable controls.
- Score tracking for both players displayed at the top of the screen.
- The ball's speed increases gradually to make the game more challenging.

## Files

- `home.py`: Contains the Ball class, which defines the ball's behavior and movement.
- `paddle.py`: Contains the Paddle class, defining the paddles for both players.
- `scoreboard.py`: Contains the Scoreboard class to display and update the scores.
- `main.py`: The main game script that sets up the game, handles player input, and manages game logic.

## Acknowledgments

- Inspired by the classic Pong game.
- 