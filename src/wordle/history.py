"""Game history persistence and statistics."""

import json

HISTORY_FILE = "history.json"

class GameHistory:
    """Store completed games and calculate player statistics."""
    def __init__(self) -> None:
        try:
            with open(HISTORY_FILE, "r") as f:
                self.games = json.load(f)

        except FileNotFoundError:
            self.games = []
            with open(HISTORY_FILE,'w') as f:
                json.dump(self.games, f, indent = 4)

    def save(self) -> None:
        with open(HISTORY_FILE,'w') as f:
            json.dump(self.games, f, indent = 4)

    def record_game(self, won: bool, attempts: int, word: str) -> None:
        self.games.append({
        "won": won,
        "attempts": attempts,
        "word": word
        })
        self.save()

    @property
    def total_games(self) -> int:
        return  len(self.games)
        
    @property
    def total_wins(self) -> int:
        count = 0

        for rec in self.games:
            if rec["won"] == True:
                count += 1
        return count

    @property
    def win_percentage(self) -> float:
        if self.total_games == 0:
            return 0
        
        return (self.total_wins / self.total_games) * 100

    @property
    def current_streak(self) -> int:
        count = 0
        if not self.games:
           return 0

        for rec in reversed(self.games):
            if rec["won"]:
               count += 1
            if not rec["won"]:
               break  
        return count             

    @property
    def best_streak(self) -> int:

        count = 0
        best = 0

        for rec in self.games:
            if rec["won"]:
                count += 1

            if not rec["won"]:
                best = max(best,count)
                count = 0

        best = max(best,count)

        return best