# Coffee-Machine

This Python program simulates a coffee machine, replicating functionalities such as coffee selection, payment processing, and drink preparation. Users can choose their desired coffee, and the machine handles payments by accepting money, checking for sufficient funds, and returning change if applicable. The program also prepares the selected coffee and includes error handling for incorrect names, insufficient funds, and ingredient availability. Additional functions and attributes ensure smooth operation by managing these aspects efficiently.

# MENU CLASS
- This file defines two classes, MenuItem and Menu, for a coffee machine simulation. The MenuItem class models individual menu items with attributes for name, cost, and ingredients (water, milk, coffee). The Menu class models the entire menu, initializing with a list of MenuItem instances (latte, espresso, cappuccino).

- The get_items function returns the names of all the items in the menu

- The find_drink function searches the menu for the drink name inputted, if the coffee is an option, we return the coffee, if not we return nothing and let the user know that the item is unavialable.

# COFFEE_MAKER CLASS
- The CoffeeMaker class models the coffee machine, managing its resources and making coffee. It has a dictionary attribute called resources, which stores the current amounts of available ingredients: water, milk, and coffee.

- The report method prints the current amounts of each resource in the machine, providing a clear overview of the machine's status.

- The is_resource_sufficient method takes a drink object as an argument and checks if the machine has enough resources to make that drink. It iterates over the ingredients required for the drink and compares them with the current resource levels. If any ingredient is insufficient, it prints a message indicating the shortage and returns False. Otherwise, it returns True, indicating that the machine can make the drink.

- Finally, the make_coffee method takes an order object as an argument and deducts the required ingredients from the machine's resources to make the coffee. It updates the resources dictionary by subtracting the amounts of each ingredient used for the order. After making the coffee, it prints a message indicating that the coffee is ready

# MONEY CLASS
- The MoneyMachine class manages financial transactions for the coffee machine. It has a CURRENCY attribute set to "$" and a COIN_VALUES dictionary that defines the value of different coin types (quarters, dimes, nickels, and pennies).

- The constructor (__init__) initializes the profit and money_received attributes to 0, tracking the total profit and money received during transactions.

- The report method prints the current profit, displaying it in the defined currency format

- The process_coins method calculates the total amount of money inserted by the user. It prompts the user to input the number of each type of coin and sums their values to update the money_received attribute

- The process_coins method calculates the total amount of money inserted by the user. It prompts the user to input the number of each type of coin and sums their values to update the money_received attribute
