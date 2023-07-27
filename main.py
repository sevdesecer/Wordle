import wordle
# clears terminal screen
import os
os.system("cls")
begin_message = """
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|                                                                          |   
|    ##        ##   #########   #########  #########  ##        ########   |
|    ##   ##   ##   ##     ##   ##     ##  ##     ##  ##        ##         |
|    ##   ##   ##   ##     ##   ##     ##  ##     ##  ##        ##         |
|    ##   ##   ##   ##     ##   ########   ##     ##  ##        ######     |
|    ##   ##   ##   ##     ##   ##   ##    ##     ##  ##        ##         |
|    ##   ##   ##   ##     ##   ##    ##   ##     ##  ##        ##         |
|      ###  ###     #########   ##     ##  #########  ########  ########   |
|                                                                          |
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

The explanation : Enter 5 letter english word. Find the right word by trial and error.Use the hints.
"""
print(begin_message.replace("#", f"{wordle.Color.YELLOW}#{wordle.Color.BASE}"))

if __name__ == '__main__':
    #with open("cheat.txt", "w") as f:  # we learn chosen word by computer.
    #   f.write(wordle.chosen_word)
    while True:
        guess = wordle.GuessWord(
            w_str=input(f"[{wordle.GuessWord.counter}] ---> ")
    )
        if guess.is_valid():
            guess.apply_guesses()
            guess.check_perfect_guess()
            guess.jump_turn()
            guess.check_game_lost()
