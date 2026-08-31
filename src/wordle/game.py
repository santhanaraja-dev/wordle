"""Core game logic for the Wordle game."""

MAX_GUESSES = 6
WORD_LENGTH = 5

def load_words() -> list[str]:
    with open("words.txt", "r") as f:
        words = f.read().splitlines()
    return words

class GuessResult:
    """Store a guessed word and its evaluation result."""
    def __init__(self, word: str, result: list[str]) -> None:
        self.word = word
        self.result = result

class Game:
    """Manage the Wordle game and evaluate player guesses."""
    def __init__(self, secret_word, word_list) -> None:
        self.secret_word = secret_word
        self.word_list = word_list
        self.guesses = []

    def evaluate_guess(self, word: str) -> GuessResult:
        """Evaluate a guess against the secret word."""
        result = ["✗"] * WORD_LENGTH
        remaining = list(self.secret_word)

        # First pass: exact matches
        for i in range(WORD_LENGTH):
            if self.secret_word[i] == word[i]:
                result[i] = "✓"
                remaining[i] = None

        # Second pass: correct letter, wrong position
        for i in range(WORD_LENGTH):
            if result[i] == "✓":
                continue

            if word[i] in remaining:
                result[i] = "~"
                remaining[remaining.index(word[i])] = None

        return GuessResult(word, result)

    def make_guess(self, word: str) -> GuessResult:

        if self.is_over:
            raise ValueError("The game is already over.")

        if len(word) != WORD_LENGTH:
            raise ValueError(f"Your guess must be {WORD_LENGTH} letters.")

        if word not in self.word_list:
            raise ValueError("Your guess is not in the word list.")
        
        guess_result = self.evaluate_guess(word)
        self.guesses.append(guess_result)
        return guess_result

    @property
    def is_won(self) -> bool:
        return bool(self.guesses) and self.guesses[-1].word == self.secret_word

    @property
    def is_over(self) -> bool:
        return self.is_won or len(self.guesses) >= MAX_GUESSES

    def __str__(self) -> str:
        board = []

        for guess in self.guesses:
            board.append(" ".join(guess.word))
            board.append(" ".join(guess.result))

        remaining_attempts = MAX_GUESSES - len(self.guesses)
        board.append(f"Remaining attempts: {remaining_attempts}")

        return "\n".join(board)

