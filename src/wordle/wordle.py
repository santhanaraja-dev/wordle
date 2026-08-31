"""Entry point for the Wordle command-line game."""

import random

from game import MAX_GUESSES, WORD_LENGTH, Game, load_words
from history import GameHistory


def main() -> None:
    word_list = load_words()
    secret_word = random.choice(word_list)

    game = Game(secret_word, word_list)
    history = GameHistory()

    while not game.is_over:
        print(game)
        guess = input(f'Enter Your Guess Word of length {WORD_LENGTH} : ')
        try:
            game.make_guess(guess)
        except ValueError as error:
            print(error)
    print(game)
    if game.is_won:
        print(f'Congratulations!!! You got it in {len(game.guesses)}/{MAX_GUESSES}!')
    else:
        print(f'The game is over & the secret word was : {secret_word}')

    history.record_game(game.is_won, len(game.guesses), secret_word)

    print(f"""************** Your_Stats *****************
            Total_games : {history.total_games}
            Total_wins : {history.total_wins}
            Win_percentage : {history.win_percentage}%
            Current_streak : {history.current_streak}
            Best_streak : {history.best_streak}"""
            )
if __name__ == "__main__":
    main()