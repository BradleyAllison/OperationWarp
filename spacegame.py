import os

def display(message):
    os.system("clear")
    print(message)

def wait_for_input():
    print("\nPress enter to continue: ", end="")
    input()

def display_options():
    display("0. Quit")

def elicit_int(lo, hi):
    while True:
        print("\nEnter an option from the menu between " + str(lo) + " and " + str(hi) + ": ", end="")
        response = input()

        if response.isdigit():
            int_response = int(response)

            if lo <= int_response and int_response <= hi:
                return int_response
            
        print("Invalid input, please enter a number from the list: ")

def elicit_menu_input():
    return elicit_int(0, 0)

def handle_main_menu_response(response):
    if response == 0:
        return True

    return False

def main_menu():
    quit = False

    while not quit:
        display_options()
        response = elicit_menu_input()
        quit = handle_main_menu_response(response)


def main():
    print("Welcome traveller, this is operation warp!\n Are you ready to travel the galaxy and make some credits?")
    wait_for_input()

    print ("Your story begins on Earth, a lone traveller with a starship ready to explore the galaxy.\n You have a small amount of credits, but need more to extend your influence.")
    wait_for_input()

    main_menu()



if __name__ == "__main__":
    main()
