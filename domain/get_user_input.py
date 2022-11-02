from options import make_coffee
from options import print_report

def get_user_option():
    option = input("Insert coffee that you want to chose: \n")
    correct_input = False
    while not correct_input:
        correct_input = True
        if option == '1':
            make_coffee.make_coffee(coffee='espresso')
        elif option == '2':
            make_coffee.make_coffee(coffee='latte')
        elif option == '3':
            make_coffee.make_coffee(coffee='cappuccino')
        elif option == 'report':
            print_report.print_report()
        elif option == 'off':
            return False
        else:
            print("incorrect input")
            correct_input = False
