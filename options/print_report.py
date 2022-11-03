from dictionaries import ingredients


def print_report():
    """Function that prints the report of
    the ingredients and money inside the machine"""
    print("--------")
    print("Report:")
    for ingredient, quantity in ingredients.machine_ingredients.items():
        print(f"{ingredient}: {quantity}")
