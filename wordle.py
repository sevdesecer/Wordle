import random
import sys
from valid_words import valid_words

chosen_word = random.choice(valid_words)
guesses_count = 6

class Color:
    PREFIX = '\033'
    BASE = "\033[0m"
    GREY = "\033[90m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    PERSISTENT_COLORS = [RED, GREEN]

class GuessWord:
    counter = 1

    # holds the string containing the guessed word.
    # The self.w_chars property splits the self.w_str string into characters and saves it as a list self.w_chars.

    def __init__(self, w_str: str):
        self.w_str = w_str
        self.w_chars = list(self.w_str)
        self.post_guess_w_str = ""

    # increase the guess counter
    def jump_turn(self):
        GuessWord.counter += 1

    def is_valid(self):
        return self.w_str in valid_words

    # for i, _ in enumerate(self.w_chars): ----> "_" means :  index is not a important variable here, enumerate independently of it.
    def apply_greens(self):
        for i, _ in enumerate(self.w_chars):
            guessed_char = self.w_chars[i]
            actual_char = chosen_word[i]
            if actual_char == guessed_char:
                colored_char = f"{Color.GREEN}{actual_char}{Color.BASE}"   # {color}{the letter whose color we want to change}{default color}
                self.w_chars[i] = colored_char

    def apply_yellow(self):
        for i, _ in enumerate(self.w_chars):
            guessed_char = self.w_chars[i]
            if guessed_char in chosen_word:
                colored_char = f"{Color.YELLOW}{guessed_char}{Color.BASE}"
                self.w_chars[i] = colored_char

    def apply_guesses(self):
        self.apply_greens()
        self.apply_yellow()
        self.post_guess_w_str = "".join(self.w_chars)
        print(self.post_guess_w_str)

    def check_perfect_guess(self):
        if self.w_str == chosen_word:
            print(f"Congratulations! You beat Wordle in {GuessWord.counter}.")
            sys.exit(1)

    def check_game_lost(self):
        if GuessWord.counter == guesses_count + 1:
            print(f"You lost the game :( The word was {Color.YELLOW}{chosen_word}{Color.BASE}.")
            sys.exit(1)
