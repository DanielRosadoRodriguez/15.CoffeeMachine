from dictionaries import coffee_current_values


def print_report():
    """Function that prints the report of
    the ingredients and money inside the machine"""
    print("--------")
    print("Report:")
    for ingredient, quantity in coffee_current_values.machine_ingredients.items():
        print(f"{ingredient}: {quantity}")
    print("--------")
