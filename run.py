import words
import random
import os


def menu_page():
    """
    Function that shows:
    the menu, the first part user will see when they start the game

    once the game ends it will return to this bit
    """

    print(f"""
Welcome to Hangman!

Please press:

1 - to look at the rules
2 - to start the game
3 - to exit the game.

Then press Enter!
    """)
    menu_choice = input("Choose an option here...\n")

    while menu_choice not in ["1", "2", "3"]:
        os.system("clear")
        print("""
Incorrect choice!

Please press:

1 - to look at the rules
2 - to start the game
3 - to exit the game.

Then press Enter!
""")
        menu_choice = input("Choose an option here...\n")

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


def which_word():
    """
    Function to see which difficulty the user would like to use,
    then returns a word based on that list
    """

    """
    Starts by asking the user for their difficulty rating
    with a while loop to make sure they choose a valid option
    """

    print("""
To start, select a difficulty rating!

1 is for easy mode
2 is for intermediate
3 is for hard mode.

Then press Enter!

""")
    difficulty_choice = input("Please select here...\n")

    while difficulty_choice not in ["1", "2", "3"]:
        print("""
Incorrect choice!

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

    if int(difficulty_choice) == 1:
        word_list = words.easy_words
    elif int(difficulty_choice) == 2:
        word_list = words.medium_words
    else:
        word_list = words.hard_words

    round_word = random.choice(word_list)

    return round_word


def choose_letter(chosen_letters):
    letter = input("Choose a letter here...\n")
    while len(letter) != 1 or ord(letter.upper()) not in range(65, 91) or letter in chosen_letters:
        if letter in chosen_letters:
            print(f"You have already chosen {letter}! Please pick a new letter")
            letter = input("Choose a letter here...\n")
        else:
            print("""
Your choice must be in the alphabet and must only be a singular letter!
""")
            letter = input("Choose a letter here...\n")

    return letter


def word_string_func(char_list):
    word = ""
    for letters in char_list:
        word += letters

    return word


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
    round_word = which_word()
    word_string = ""
    char_list = []

    for letters in round_word:
        char_list.append("-")

    print("Let's begin!")
    word_string = word_string_func(char_list)

    """
    loop for if the game has finished,
    if it hasn't the first thing it does is ask the user for a letter
    """

    while lives > 0 and "-" in char_list:
        print(f"Your word so far is {word_string}, lives left: {lives}")
        letter_choice = choose_letter(chosen_letters)
        letter_choice = letter_choice.lower()
        chosen_letters.append(letter_choice)
        if letter_choice not in round_word:
            lives -= 1
        else:
            for letter in range(0, len(round_word)):
                if round_word[letter] == letter_choice:
                    char_list[letter] = letter_choice
                    word_string = word_string_func(char_list)

    if lives > 0:
        print(f"Congratulations, you have won! The word was {round_word}")
    else:
        print(f"Oh no! You lost! the word was {round_word}")


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
            print("""
Thank you for playing hangman! Please press H to go back to the home page.
""")
            back_home = input("Enter here...\n")

            while back_home.upper() != "H":
                print("""
Incorrect choice, please press H to go back to the home page.
""")
                back_home = input("Enter here...\n")

        menu_choice = menu_page()

    print("""
Thank you for playing hangman! See you next time!
""")


if __name__ == "__main__":
    main()
