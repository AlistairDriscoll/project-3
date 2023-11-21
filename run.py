import words

print("Welcome to Hangman!")

def menu_page():
    """
    Function that shows the menu, the first part user will see when they start the game, once the game ends it will return to this bit
    """
    
    print(f"\nPlease press 1 to look at the rules, 2 to start the game, or 3 to exit the game.\n")
    menu_choice = input("Choose an option here...")

    while menu_choice not in ["1", "2", "3"]:
        print(f"Incorrect choice, please press 1 to look at the rules, 2 to start the game, or 3 to exit the game.\n")
        menu_choice = input("Choose an option here...")
        
    return menu_choice


def rules_page():
    """
    Function to display the rules
    """

    print("""
Hangman is a game of guessing.
You can choose a difficulty rating and you will be given an easier or harder word to guess depending on what you have chosen.
At first you will not know any of the letters and will have to guess what they are.
Make sure to choose carefully as you will only have ten guesses until you lose the game!
If you guess the full word before you run out of guesses, you win!
""")
    
    go_to_menu = input("Press b to go back to the menu page...")
    while go_to_menu.upper() != "B":
        print("Incorrect input, please select b to go to the game.")
        go_to_menu = input("Select here...")

    
        



def game_page():
    """Function to start the game itself"""
    print("Here is the game")


def main():
    """
    Function that controls where the user goes next, depending on their option, making sure they havent typed in an invalid choice
    """
    menu_choice = menu_page()

    while int(menu_choice) != 3:
        if int(menu_choice) == 1:
            print("You chose to see the rules!")
            rules_page()
            
        elif int(menu_choice) == 2:
            print("Your chose to start the game!")
            game_page()
        
        menu_choice = menu_page()

    print("Thank you for playing hangman!")
        
    
    



main()


