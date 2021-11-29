from interface import *
from travel_menu import travel_menu

import planet

def display_options():
    display_str = planet.description()
    display_str += " 1. Travel\n"
    display_str += " 0. Quit"

    display(display_str)

def elicit_menu_input():
    return elicit_int(0, 1)

def handle_main_menu_response(response):
    if response == 0:
        return True
    elif response == 1:
        travel_menu()

    return False

def main_menu():
    quit = False

    while not quit:
        display_options()
        response = elicit_menu_input()
        quit = handle_main_menu_response(response)
