from options import make_coffee
from options import print_report
from dictionaries import coins as c

coffee = 100
milk = 200
water = 300


def get_user_option():

    correct_input = False
    while not correct_input:
        option = input("Insert coffee that you want to chose: \n")
        if option == '1':
            make_coffee.make_coffee(coffee_type='espresso')
            return True
        elif option == '2':
            make_coffee.make_coffee(coffee_type='latte')
            return True
        elif option == '3':
            make_coffee.make_coffee(coffee_type='cappuccino')
            return True
        elif option == 'report':
            print_report.print_report()
            return True
        elif option == 'off':
            return False
        else:
            print("incorrect input")
            correct_input = False


def get_coins():
    pennys = int(input("How many Penny?: "))
    nickels = int(input("How many Nickels?: "))
    dimes = int(input("How many Dimes?: "))
    quarters = int(input("How many Quarters?: "))
    money = pennys*c.coins['penny'] + nickels*c.coins['nickel'] + dimes*c.coins['dime'] + quarters*c.coins['quarter']

    return money
