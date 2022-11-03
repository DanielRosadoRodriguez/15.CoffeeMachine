from dictionaries import coffee_types
from dictionaries import coffee_current_values
from domain import get_user_input as gui


def make_coffee(coffee_type):
    """
    receives what type of coffee the user wants and makes it
    :return:
    """

    water_required = coffee_types.menu[coffee_type]['ingredients']['water']
    milk_required = coffee_types.menu[coffee_type]['ingredients']['milk']
    coffee_required = coffee_types.menu[coffee_type]['ingredients']['coffee']
    money_required = coffee_types.menu[coffee_type]['price']

    c_water = coffee_current_values.machine_ingredients['water']
    c_milk = coffee_current_values.machine_ingredients['milk']
    c_coffee = coffee_current_values.machine_ingredients['coffee']
    c_coins = coffee_current_values.machine_ingredients['coins']

    new_water = c_water - water_required
    new_milk = c_milk - milk_required
    new_coffee = c_coffee - coffee_required
    money_given = gui.get_coins()
    return_money = money_given - money_required

    if return_money < 0:
        print("Insufficient money")
    elif new_water < 0:
        print("Insufficient water")
    elif new_milk < 0:
        print("Insufficient milk")
    elif new_coffee < 0:
        print("Insufficient coffee")
    else:
        print(f"Making {coffee_type}")
        coffee_current_values.machine_ingredients['water'] = new_water
        coffee_current_values.machine_ingredients['milk'] = new_milk
        coffee_current_values.machine_ingredients['coffee'] = new_coffee
        coffee_current_values.machine_ingredients['coins'] = c_coins + money_required
        print(f"exchange: {return_money}")
