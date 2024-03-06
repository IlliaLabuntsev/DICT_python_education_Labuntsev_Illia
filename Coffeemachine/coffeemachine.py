"""Coffeemachine project"""


class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550

    def show_available_ingredients(self):
        """
            This method shows the available ingredients in the coffe machine
            Params: none

            Returns: none
        """
        print(f"The coffee machine has:\n"
              f"{self.water} of water\n"
              f"{self.milk} of milk\n"
              f"{self.coffee_beans} of coffee beans\n"
              f"{self.disposable_cups} of disposable cups\n"
              f"{self.money} of money")

    def buy_coffee(self, coffee_type_param):
        """
            This method is used to buy a coffee

            Params:
            int(coffee_type_param): selected coffee type

            Returns:
            None
        """
        if coffee_type_param == 1:  # Espresso
            water_needed = 250
            beans_needed = 16
            milk_needed = 0
            cost = 4
        elif coffee_type_param == 2:  # Latte
            water_needed = 350
            milk_needed = 75
            beans_needed = 20
            cost = 7
        elif coffee_type_param == 3:  # Cappuccino
            water_needed = 200
            milk_needed = 100
            beans_needed = 12
            cost = 6
        else:
            print("Invalid coffee type. Please choose 1, 2, or 3.")
            return

        if self.water >= water_needed and self.milk >= milk_needed and \
                self.coffee_beans >= beans_needed and self.disposable_cups >= 1:
            print("I have enough resources, making your coffee!")
            self.water -= water_needed
            self.milk -= milk_needed
            self.coffee_beans -= beans_needed
            self.disposable_cups -= 1
            self.money += cost
            print(f"Here is your {['Espresso', 'Latte', 'Cappuccino'][coffee_type_param - 1]}. Enjoy!")
        else:
            print("Not enough resources to make the coffee.")

    def fill_machine(self, water_param, milk_param, coffee_beans_param, disposable_cups_param):
        """
            This method fills the resources to machine
            Params:
            int(water_param): amount of water that left,
            int(milk_param): amount of milk that left,
            int(coffee_beans_param): amount of coffee beans that left,
            int(disposable_cups_param): amount of disposable cups that left

            Returns: none
        """
        self.water += water_param
        self.milk += milk_param
        self.coffee_beans += coffee_beans_param
        self.disposable_cups += disposable_cups_param

    def take_money(self):
        """
            This method takes money from coffeemachine
            Params: none
            Returns: none
        """
        print(f"I gave you {self.money}")
        self.money = 0


coffee_machine = CoffeeMachine()

while True:
    action = input("Write action (buy, fill, take, remaining, exit): ")

    if action == 'buy':
        while True:
            coffee_type = input(
                "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")

            if coffee_type == 'back':
                break

            coffee_type = int(coffee_type)

            if 1 <= coffee_type <= 3:
                coffee_machine.buy_coffee(coffee_type)
                break
            else:
                print("Invalid coffee type. Please choose 1, 2, 3, or back.")

    elif action == 'fill':
        water = int(input("Enter the amount of water to add: "))
        milk = int(input("Enter the amount of milk to add: "))
        coffee_beans = int(input("Enter the amount of coffee beans to add: "))
        disposable_cups = int(input("Enter the number of disposable cups to add: "))
        coffee_machine.fill_machine(water, milk, coffee_beans, disposable_cups)

    elif action == 'take':
        coffee_machine.take_money()

    elif action == 'remaining':
        coffee_machine.show_available_ingredients()

    elif action == 'exit':
        print('Bye!')
        break
    else:
        print("Invalid action. Please choose buy, fill, take, remaining, or exit.")
