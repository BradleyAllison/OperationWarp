import os

def display_story(message):
    os.system("clear")
    print(message)

def wait_for_input():
    print("\nPress enter to continue: ", end="")
    input()

def main():
    print("Welcome traveller, this is operation warp!\n Are you ready to travel the galaxy and make some credits?")
    wait_for_input()

    print ("Your story begins on Earth, a lone traveller with a starship ready to explore the galaxy.\n You have a small amount of credits, but need more to extend your influence.")
    wait_for_input()





if __name__ == "__main__":
    main()
