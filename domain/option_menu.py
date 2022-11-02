from dictionaries import coffee_types


def option_menu():
    """
    function that prints the option menu
    receives the user input and validates it
    transforms the input into a number and returns it
    :return: option
    """
    print(f"What type of coffee do you want?")
    for i, coffee in enumerate(coffee_types.menu):
        print(f"{i+1} - {coffee.title()}")
