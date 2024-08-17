# Coffee Machine

This Python program simulates a coffee machine, handling functionalities such as coffee selection, payment processing, and drink preparation. Users can choose their desired coffee, and the machine manages payments, checks for sufficient funds, and prepares the selected coffee. The program includes error handling for incorrect names, insufficient funds, and ingredient availability.

## Components

### Menu Class

The `Menu` class defines the available coffee options and their attributes.

- **`MenuItem` Class**: Represents an individual menu item with attributes for name, cost, and ingredients (water, milk, coffee).

- **`Menu` Class**: Manages the list of `MenuItem` instances (latte, espresso, cappuccino).

  - **`get_items()`**: Returns the names of all items in the menu.
  
  - **`find_drink(name)`**: Searches for a drink by name. If the drink is available, it returns the corresponding `MenuItem` object; otherwise, it notifies the user that the item is unavailable.

### Coffee Maker Class

The `CoffeeMaker` class models the coffee machine, handling resources and drink preparation.

- **`resources`**: A dictionary storing the current amounts of available ingredients (water, milk, coffee).

- **`report()`**: Prints the current amounts of each resource, providing an overview of the machine's status.

- **`is_resource_sufficient(drink)`**: Checks if the machine has enough resources to make the requested drink. It compares the required ingredients with the available resources and prints a message if any ingredient is insufficient. Returns `True` if the resources are sufficient, otherwise `False`.

- **`make_coffee(drink)`**: Deducts the required ingredients from the machine’s resources and prepares the coffee. Prints a message indicating that the coffee is ready.

### Money Machine Class

The `MoneyMachine` class handles financial transactions for the coffee machine.

- **`CURRENCY`**: Set to "$", defines the currency format.

- **`COIN_VALUES`**: A dictionary defining the value of different coin types (quarters, dimes, nickels, pennies).

- **`profit`**: Tracks the total profit from transactions.

- **`money_received`**: Tracks the total money received during transactions.

- **`report()`**: Prints the current profit in the defined currency format.

- **`process_coins()`**: Calculates the total amount of money inserted by the user. Prompts the user to input the number of each coin type, sums their values, and updates the `money_received` attribute.

## How to Run

To run the coffee machine simulation, ensure you have Python installed on your system. Execute the main Python script to start the program.
