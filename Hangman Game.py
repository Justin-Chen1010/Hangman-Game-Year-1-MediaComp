# import file to be able to use random function
import random

# import countries file and make it a list
file = open("countries.txt")
country_list = []
for country in file.readlines():
    country_list.append(country.strip("\n"))
file.close()

# set function to return the coordinate of the letter
def letter_check(guess_letter, hidden_word):
    coordinates = []
    for i in range(len(hidden_word)):
        if hidden_word[i] == guess_letter:
            coordinates.append(i)
    return coordinates

# set variable to randomly pick number out of 162 (because there is 162 countries in the list)
random_num = random.randrange(1,162)

# set the hidden word, coverts it to lower case.
hidden_word = country_list[random_num]
hidden_word_1 = hidden_word.lower()

# sets number of attempts and opens output list
attempts = 10
output_list = []

# create function to replace the letter with the correct position
def player_progress(guess_letter, output, output_list):
    for word_pos in letter_check(guess_letter, hidden_word_1):
        output_list[word_pos] = guess_letter
    for letter in output_list:
        output += letter
    return output


# create the hangman format
for word in range(len(hidden_word_1)):
    output_list.append(" _ ")

# main portion of the game, this loop prompts user to guess a letter.
while attempts != 0:
    output = ""
    guess_letter = input("Guess a letter: ")
# converts the guessed letter to lower because hidden word is converted to lower
    guess_letter = guess_letter.lower()

# returns error message for an invalid input (ex: number, symbols, two letters or input space).
    if not guess_letter.isalpha() or len(guess_letter) > 1 or (guess_letter == " "):
        attempts +=1
        print("Please enter a valid letter!")

# checks if the user guesses the right letter and if so outputs the attempts and progress.
    if guess_letter in hidden_word_1:
        progress = player_progress(guess_letter, output, output_list)
# prints the progress with the first letter capitalized because it was changed to lower
        progress = progress.capitalize()
        print(f"Word: '{progress}' Nice! You have {attempts} attempts left.")

# if user guesses wrong letter it subtracts their attempts and they can see their progress
    else:
        progress = player_progress(guess_letter, output, output_list)
        progress = progress.capitalize()
        attempts -= 1
        print(f"Word: '{progress}' you have guessed the wrong letter (Hint: It's a country), you have {attempts} attempts left.")

# tell the user they won!
    if progress == hidden_word:
        print(f"You win! The hidden country was indeed: {hidden_word}")
        break


# tell the user they lost and the correct word.
if output !=hidden_word and attempts == 0:
    print("You lost. The hidden country was: " + hidden_word)


