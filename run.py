print("Welcome to Hangman!")

def menu_page():
    """Function that shows the first thing the user will see when they start the game, once the game ends it will return to this bit"""
    
    print(f"\nPlease press 1 to look at the rules or 2 to start the game.\n")
    menu_choice = input("Please choose an option...")
    return menu_choice


def rules_page():
    """Function to display the rules and either take the user back to the menu page or carry on to the game"""
    print("Here are the rules")

def game_page():
    """Function to start the game itself"""
    print("Here is the game")

menu_choice = menu_page()

while menu_choice not in ['1', '2']:
    print("Incorrect option, please choose again...")
    menu_choice = menu_page()

if int(menu_choice) == 1:
    rules_page()
elif int(menu_choice) == 2:
    game_page()





