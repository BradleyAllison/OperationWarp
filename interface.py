import os

def display(message):
    os.system("clear")
    print(message)

def wait_for_input():
    print("\nPress enter to continue: ", end="")
    input()

def elicit_int(lo, hi):
    while True:
        print("\nEnter an option from the menu between " + str(lo) + " and " + str(hi) + ": ", end="")
        response = input()

        if response.isdigit():
            int_response = int(response)

            if lo <= int_response and int_response <= hi:
                return int_response
            
        print("Invalid input, please enter a number from the list: ")

