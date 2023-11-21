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

def which_word():
    """
    Function to see which difficulty the user would like to use, then returns a word based on that list
    """


    # Starts by asking the user for their difficulty rating, with a while loop to make sure they choose a valid option

    print("To start, select a difficulty rating! 1 is for easy mode, 2 is for intermediate, and 3 is for hard mode.")
    difficulty_choice = input("Please select here...")

    while difficulty_choice not in ["1", "2", "3"]:
        print("Incorrect choice, select either 1 for easy difficulty, 2 for intermediate or 3 for hard difficulty")
        difficulty_choice = input("Please select here...")

    
    # then assigns a list of words depending on difficulty rate chosen and selects a random word from that list to use

    if int(difficulty_choice) == 1:
        word_list = words.easy_words
    elif int(difficulty_choice) == 2:
        word_list = words.medium_words
    else:
        word_list = words.hard_words

    round_word = random.choice(word_list)

    return round_word

def choose_letter():
    letter = input("Choose a letter here...")
    while len(letter) != 1 or ord(letter.upper()) not in range(65, 91):
        print("Your choice must be in the alphabet and must only be a singular letter!")
        letter = input("Choose a letter here...")

    return letter

def game_page():
    """
    Function to start the game itself
    The variable declarations are at the top
    round_word is the word of the round, word_string is what the user will see while they are playing the game
    The function starts with seven lives
    """
    
    lives = 7
    round_word = which_word()
    word_string = ""
    for letters in round_word:
        word_string += "-"
    result = f"Your word so far is: {word_string} lives left: {lives}"


    print(f"\nLet's begin!\n")

    # loop for if the game has finished, if it hasn't the first thing it does is ask the user for a letter
    while lives > 0 or "-" not in word_string:
        letter_choice = choose_letter()
        if letter_choice not in round_word:
            lives =- 1



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


