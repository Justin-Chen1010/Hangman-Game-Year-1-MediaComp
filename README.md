# Hangman Game Year 1 Media Computation

**Version 1.0.0**

This program is a minigame coded in Python, it's a simple hangman game that I made in first year semester 1 when I first started out coding. It takes a list of countries from the textfile and randomly picks one. You are first prompted to guess a letter and if you guessed one of the correct ones it will output the up to date guessing word in a hangman format.

## Example: 

You run the program with the command
```
python3 "Hangman Game.py"
```
Then the program responds with:
```
Guess a letter:
```
After guessing a letter it will respond with either
```
Word: ' _  _  _  _  _ ' you have guessed the wrong letter (Hint: It's a country), you have `8` attempts left.
```
Or 
```
Word: ' _  _ i _  _ ' Nice! You have `8` attempts left.
```
and when you win the game the output is
```
Word: 'Chile' Nice! You have `5` attempts left.
You win! The hidden country was indeed: Chile
```