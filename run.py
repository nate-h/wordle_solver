import json
import os
import time
import random


class WordleSolver:
    """Plan
    1. Takes just commands
    2. Play takes just guesses
    3. Render results
    4. how to play game
    5. explanation of outcome, guess
    6. Hint module
    7. Only letters and 1 comma
    """
    def __init__(self):
        self.modes = ["wordle", "clear"]
        self.mode = self.modes[0]
        with open("five_letter_words.json") as json_file:
            self.full_dict = set(json.load(json_file))
        self.max_guesses = 6
        self.reset()
        self.play()

    def reset(self):
        self.words = self.full_dict
        self.guesses = []
        self.outputs = []

    def play(self):
        """Play wordle as a command line game."""

        #word = random.choice(tuple(self.full_dict))
        word = "those"
        self.reset()

        while True:
            self.clear_screen()
            print(f"Mode: {self.mode}")
            print(f"Word count: {len(self.words)}")
            print(f"Guesses left: {self.max_guesses - len(self.guesses)}")
            print("---")
            print(f"Guesses: {self.guesses}")
            print(f"Outputs: {self.outputs}")
            print("---")
            guess = input("Make a guess or enter a command: ")

            # Validate guess.
            if self.validate_guess(guess):
                self.guesses.append(guess)
            else:
                time.sleep(1.5)
                continue

            # Process guess.
            self.outputs.append(self.generate_comparison(word, guess))
            if guess == word:
                self.win_message(word)
                self.play()
            elif len(self.guesses) > self.max_guesses:
                self.lose_message(word)
                self.play()

    def validate_guess(self, guess: str) -> bool:
        """Ensure guess is a valid 5 letter word."""
        guess = guess.lower()
        if len(guess) != 5:
            print("Incorrect Length. Guess again!")
            return False
        if not guess.isalpha():
            print("Guesses can only contain letters. Guess again!")
            return False
        if guess not in self.full_dict:
            print("Guesses can only be valid 5 letter words. Guess again!")
            return False
        return True

    def generate_comparison(self, word: str, guess: str) -> str:
        """Returns 5 character string representing the comparison between the
        word and guess. Characters that are in the right position will be
        marked with a "c". Characters in the wrong position but present in the
        word will be marked with an "i". Characters not in the final string
        will be marked with a "_".
        """
        ret = []
        for i, g in enumerate(guess):
            if g == word[i]:
                ret.append("c")
            elif g in word:
                ret.append("i")
            else:
                ret.append("_")
        return "".join(ret)


    def clear_screen(self):
        """Clear screen. OS type dictates system call so this checks for that."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def help(self):
        print(f"Word Count: {len(self.dict)}")

    def parse_input(self):
        flags = ["dict", "undo", "reset", "play", "wordle", "hint"]

    def hint(self):
        return self.dict[0]

    def win_message(self, word: str):
        """Clears screen and displays win message."""
        self.clear_screen()
        print(
            f"DING DING DING! '{word}' is correct.\n"
            f"You Won in {len(self.guesses)} guesses!\n"
            "---\n"
            f"Guesses: {self.guesses}\n"
            f"Outputs: {self.outputs}\n"
        )
        input("Press any key to play again.")

    def lose_message(self, word: str):
        """Clears screen and displays lose message."""
        self.clear_screen()
        print(
            f"WOMP WOMP! '{word}' was the word.\n"
            "You Lose!\n"
            "---\n"
            f"Guesses: {self.guesses}\n"
            f"Outputs: {self.outputs}\n"
        )
        input("Press any key to play again.")


if __name__ == "__main__":
    WordleSolver()

##########################################

""" Commands

WORDLE - play alongside website

dict - view all words
guess, outcome
undo
reset - reset and set mode to wordle solve
play - reset mode to play
wordle - reset mode to wordle
hint - intelligent guess

------------------------------------------

PLAY: play without website

Same as wordle but: don't enter outcome, no undo


"""


