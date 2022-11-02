from dictionaries import coffee_types


def make_coffee(coffee_type, c_water, c_milk, c_coffee):
    """
    receives what type of coffee the user wants and makes it
    :return:
    """

    water_required = coffee_types.menu[coffee_type]['ingredients']['water']
    milk_required = coffee_types.menu[coffee_type]['ingredients']['milk']
    coffee_required = coffee_types.menu[coffee_type]['ingredients']['coffee']

    new_water = c_water - water_required
    new_milk = c_milk - milk_required
    new_coffee = c_coffee - coffee_required

    if new_water < 0:
        print("Insufficient water")
        return c_water, c_milk, c_coffee
    elif new_milk < 0:
        print("Insufficient milk")
        return c_water, c_milk, c_coffee
    elif new_coffee < 0:
        print("Insufficient coffee")
        return c_water, c_milk, c_coffee
    else:
        print(f"Making {coffee_type}")
        return new_water, new_milk, new_coffee
