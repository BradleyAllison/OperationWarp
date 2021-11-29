from interface import *
import planet

def display_options():
    display_str = planet.travel_targets()
    display_str += " 0. Cancel Travel"

    display(display_str)

def elicit_menu_input():
    return elicit_int(0, planet.total_planets() - 1)

def handle_main_menu_response(response):
    if response == 0:
        return True
    else:
        ship.travel_to(response)

    return False

def travel_menu():
    quit = False

    while not quit:
        display_options()
        response = elicit_menu_input()
        quit = handle_main_menu_response(response)
