from domain import print_startup_messages as pm
from domain import option_menu as om
from domain import get_user_input as gui

pm.print_startup_message()

while True:
    om.option_menu()
    keep_on = gui.get_user_option()
    if not keep_on:
        print("turning off machine...")
        break
