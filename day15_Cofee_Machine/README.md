```markdown
# Coffee Machine Simulator in Python

This Python script simulates a basic coffee machine that can serve espresso, latte, and cappuccino. Users can interact with the coffee machine by following the prompts in the terminal.

## Prerequisites

- Python 3.x

## How to Run

1. Download the project files to your local machine.

2. Open a terminal and navigate to the project directory.

3. Run the project using the following command:

   ```bash
   python main.py
   ```

## Usage

The coffee machine simulator provides the following features:

1. **Prompt for User Input:** When you run the `main.py` script, it will prompt you with the message: "What would you like? (espresso/latte/cappuccino):"

2. **Turn Off the Coffee Machine:** To turn off the coffee machine, simply type "off" in response to the prompt.

3. **Print Report:** Typing "report" at the prompt will display a report of the current resources (water, coffee beans, milk, and money).

4. **Check Resources:** Before making a coffee, the script checks if there are enough resources available.

5. **Process Coins:** When prompted, enter the number of quarters, dimes, nickels, and pennies to pay for the selected coffee.

6. **Check Transaction Success:** The script checks if the entered coins are sufficient to make the selected coffee. If the payment is successful, it calculates the change and adds the money to the machine's balance.

7. **Make Coffee:** If all conditions are met (sufficient resources and successful payment), the script prepares and serves the selected coffee.

## Example Usage

Here's an example of how to use the coffee machine simulator:

1. When prompted, enter "espresso" to order an espresso.

2. Follow the prompts to enter the required coins (quarters, dimes, nickels, and pennies).

3. If there are enough resources and the payment is successful, the script will make and serve the espresso.

4. You can also check the available resources or turn off the machine at any time.
