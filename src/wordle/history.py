"""Game history persistence and statistics."""

import json

HISTORY_FILE = "history.jsonl"


class GameHistory:
    """Store completed games and calculate player statistics."""

    def __init__(self) -> None:
        self.games = []

        try:
            with open(HISTORY_FILE, "r") as f:
                for line in f:
                    if line.strip():
                        self.games.append(json.loads(line))

        except FileNotFoundError:
            pass

    def record_game(self,won: bool,attempts: int,word: str,) -> None:
        """Append a completed game to the history file."""

        game = {
            "won": won,
            "attempts": attempts,
            "word": word,
        }

        # Keep the current session's history in memory
        self.games.append(game)

        # Append only the new game to the file
        with open(HISTORY_FILE, "a") as f:
            json.dump(game, f)
            f.write("\n")

    @property
    def total_games(self) -> int:
        """Return the total number of games played."""
        return len(self.games)

    @property
    def total_wins(self) -> int:
        """Return the total number of games won."""
        return sum(rec["won"] for rec in self.games)

    @property
    def win_percentage(self) -> float:
        """Return the percentage of games won."""

        if self.total_games == 0:
            return 0.0

        return (self.total_wins / self.total_games) * 100

    @property
    def current_streak(self) -> int:
        """Return the current winning streak."""

        count = 0

        for rec in reversed(self.games):
            if not rec["won"]:
                break

            count += 1

        return count

    @property
    def best_streak(self) -> int:
        """Return the longest winning streak."""

        count = 0
        best = 0

        for rec in self.games:
            if rec["won"]:
                count += 1
                best = max(best, count)
            else:
                count = 0

        return best