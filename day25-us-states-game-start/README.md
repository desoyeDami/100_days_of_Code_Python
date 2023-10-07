# U.S. States Game

The U.S. States Game is a Python program that allows you to learn and test your knowledge of the U.S. states by guessing their names on a map.

## Description

The program uses the Turtle graphics library to display a map of the United States with blank state names. You can input the names of the states you know, and the program will display the names on the map. The goal is to guess all 50 U.S. states correctly.

## Features

- Interactive and educational game.
- Utilizes the Turtle graphics library for graphical display.
- Keeps track of the guessed states.
- Exports a list of missed states to a CSV file for further learning.

## How to Use

1. Install Python if not already installed on your system.

2. Clone this repository or download the source code.

3. Ensure you have the required dependencies, `turtle` and `pandas`, installed. You can install them using pip:

   ```
   pip install turtle pandas
   ```

4. Run the program:

   ```
   python main.py
   ```

5. The game will start, and you will be prompted to enter the names of U.S. states that you know.

6. To exit the game, type "Exit" when prompted for a state name.

7. After playing, a CSV file named "learn.csv" will be generated, containing a list of states you missed for further learning.

## Requirements

- Python 3.x
- turtle library
- pandas library

## Acknowledgments

- This program was created as a learning project.
- The U.S. states data used in this program is from the "50_states.csv" file.
