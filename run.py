import words
import random
import os

#TODO add lives icons, display of hangman stages, change lives amount, colours

def menu_page():
    """
    Function that shows:
    the menu, the first part user will see when they start the game

    once the game ends it will return to this bit
    """

    print(f"""Welcome to Hangman!

Please press:

1 - to look at the rules
2 - to start the game
3 - to exit the game.

Then press Enter!
    """)
    menu_choice = input("Choose an option here...\n")

    while menu_choice not in ["1", "2", "3"]:
        os.system("clear")
        print("""Incorrect choice!

Please press:

1 - to look at the rules
2 - to start the game
3 - to exit the game.

Then press Enter!
""")
        menu_choice = input("Choose an option here...\n")

    os.system("clear")
    return menu_choice


def rules_page():
    """ Function to display the rules """

    print("""
THE RULES:

Hangman is a game of guessing.
You can choose a difficulty rating and you will be given an easier or harder
word to guess depending on what you have chosen.
At first you will not know any of the letters
and will have to guess what they are.
Make sure to choose carefully as you will only have
seven guesses until you lose the game!
If you guess the full word before you run out of guesses, you win!
""")

    go_to_menu = input("Press b to go back to the menu page...\n")
    while go_to_menu.upper() != "B":
        print("""
Incorrect input, please select b to go back to the menu.
""")
        go_to_menu = input("Select here...\n")

    os.system("clear")


def which_word():
    """
    Function to see which difficulty the user would like to use,
    then returns a word based on that list
    """

    """
    Starts by asking the user for their difficulty rating
    with a while loop to make sure they choose a valid option
    """

    print("""To start, select a difficulty rating!

1 is for easy mode
2 is for intermediate
3 is for hard mode.

Then press Enter!

""")
    difficulty_choice = input("Please select here...\n")

    while difficulty_choice not in ["1", "2", "3"]:
        os.system("clear")
        print("""Incorrect choice!

Select either:

1 for easy difficulty
2 for intermediate or
3 for hard difficulty

Then press Enter
""")
        difficulty_choice = input("Please select here...\n")

    """
    Then assigns a list of words depending on difficulty rate chosen
    and selects a random word from that list to use
    """

    os.system("clear")

    if int(difficulty_choice) == 1:
        word_list = words.easy_words
        mode = "easy"
    elif int(difficulty_choice) == 2:
        word_list = words.medium_words
        mode = "intermediate"
    else:
        word_list = words.hard_words
        mode = "hard"

    round_word = random.choice(word_list)

    return round_word, mode


def choose_letter(chosen_letters, word_string, lives):
    letter = input("Choose a letter here...\n")
    while len(letter) != 1 or ord(letter.upper()) not in range(65, 91) or letter in chosen_letters:
        os.system("clear")
        if letter in chosen_letters:
            print(f"""
You have already chosen {letter}! Please pick a new letter.

Your word so far is {word_string}. Lives: {lives}.
""")
            letter = input("Choose a letter here...\n")
        else:
            print("""
Your choice must be in the alphabet and must only be a singular letter!

Your word so far is {word_string}. Lives: {lives}.
""")
            letter = input("Choose a letter here...\n")

    os.system("clear")

    print(f"You have chosen {letter}!")
    return letter


def word_string_func(char_list):
    word = ""
    for letters in char_list:
        word += letters

    return word


def return_home_func():
    print("""
Thank you for playing hangman! Please press H to go back to the home page.
""")
    back_home = input("Enter here...\n")

    while back_home.upper() != "H":
        print("""You didn't select H!

Incorrect choice, please press H to go back to the home page.
""")
        back_home = input("Enter here...\n")


def game_page():
    """
    Function to start the game itself
    The variable declarations are at the top
    round_word is the word of the round, char_list is the list of the guessed
    and unguessed letters, the unguessed ones being hyphons
    word_string is the list of guessed and unguessed letters put together as a
    word to display to the user
    The function starts with seven lives
    """

    lives = 7
    chosen_letters = []
    round_word, mode = which_word()
    word_string = ""
    char_list = []

    for letters in round_word:
        char_list.append("-")

    print(f"You chose {mode} mode! Let's begin!\n")
    word_string = word_string_func(char_list)

    """
    loop for if the game has finished,
    if it hasn't the first thing it does is ask the user for a letter
    """

    while lives > 0 and "-" in char_list:
        print(f"""Your word so far is {word_string}
lives left: {lives}
""")

        letter_choice = choose_letter(chosen_letters, word_string, lives)
        letter_choice = letter_choice.lower()
        chosen_letters.append(letter_choice)
        if letter_choice not in round_word:
            lives -= 1
            print(f"""
Oh no! {letter_choice} was not in the word! You have {lives} lives left.
""")
        else:
            for letter in range(0, len(round_word)):
                if round_word[letter] == letter_choice:
                    char_list[letter] = letter_choice
                    word_string = word_string_func(char_list)
                    print(f"""
Well done! {letter_choice} was in the word! Your word is now {word_string}.
Lives left: {lives}. Keep it up!
""")

    os.system("clear")

    if lives > 0:
        print(f"Congratulations, you have won! The word was {round_word}!")
    else:
        print(f"Oh no! You lost! the word was {round_word}!")


def main():
    """
    Function that controls where the user goes next, depending on their option
    making sure they havent typed in an invalid choice
    """
    menu_choice = menu_page()

    while int(menu_choice) != 3:
        if int(menu_choice) == 1:
            print("You chose to see the rules!")
            rules_page()
        elif int(menu_choice) == 2:
            print("Your chose to start the game!")
            game_page()
            return_home_func()

        os.system("clear")

        menu_choice = menu_page()

    print("""You chose to exit!

Thank you for playing hangman! See you next time!
""")


if __name__ == "__main__":
    main()
