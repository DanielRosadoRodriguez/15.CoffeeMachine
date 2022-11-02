from options import make_coffee
from options import print_report

coffee = 100
milk = 200
water = 300


def get_user_option():

    correct_input = False
    while not correct_input:
        option = input("Insert coffee that you want to chose: \n")
        correct_input = True
        if option == '1':
            make_coffee.make_coffee(coffee_type='espresso', c_coffee=coffee, c_water=water, c_milk=milk)
            return True
        elif option == '2':
            make_coffee.make_coffee(coffee_type='latte', c_coffee=coffee, c_water=water, c_milk=milk)
            return True
        elif option == '3':
            make_coffee.make_coffee(coffee_type='cappuccino', c_coffee=coffee, c_water=water, c_milk=milk)
            return True
        elif option == 'report':
            print_report.print_report()
            return True
        elif option == 'off':
            return False
        else:
            print("incorrect input")
            correct_input = False
