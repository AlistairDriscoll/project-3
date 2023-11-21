import words
import random

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
Make sure to choose carefully as you will only have seven guesses until you lose the game!
If you guess the full word before you run out of guesses, you win!
""")
    
    go_to_menu = input("Press b to go back to the menu page...")
    while go_to_menu.upper() != "B":
        print("Incorrect input, please select b to go to the game.")
        go_to_menu = input("Select here...")


def game_page():
    """
    Function to start the game itself
    """

    # Starts by asking the user for their difficulty rating, with a while loop to make sure they choose a valid option

    print("To start, select a difficulty rating! 1 is for easy mode, 2 is for intermediate, and 3 is for hard mode.")
    difficulty_choice = input("Please select here...")

    while difficulty_choice not in ["1", "2", "3"]:
        print("Incorrect choice, select either 1 for easy difficulty, 2 for intermediate or 3 for hard difficulty")
        difficulty_choice = input("Please select here...")
        difficulty_choice = int(difficulty_choice)
        
    if difficulty_choice == 1:
        word_list = words.easy_words
    elif difficulty_choice == 2:
        word_list = words.medium_words
    else:
        word_list = words.hard_words

    round_word = random.choice(word_list)

    


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


