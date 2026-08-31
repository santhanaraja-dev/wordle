import pytest

from wordle.game import Game


def test_evaluate_guess_fully_correct():
    game = Game("apple", ["apple"])
    result = game.evaluate_guess("apple")
    assert result.result == ["✓", "✓", "✓", "✓", "✓"]

def test_evaluate_guess_mixed():
    game = Game("apple", ["apple", "pleat"])
    result = game.evaluate_guess("pleat")
    assert result.result == ["~", "~", "~", "~", "✗"]

def test_evaluate_guess_duplicate_letters():
    game = Game("apple", ["apple", "allel"])
    result = game.evaluate_guess("allel")
    assert result.result == ["✓", "~", "✗", "~", "✗"]

def test_make_guess_invalid_word():
    game = Game("apple", ["apple"])
    with pytest.raises(ValueError):
        game.make_guess("allel")

def test_game_is_won_after_correct_guess():
    game = Game("apple", ["apple"])
    game.make_guess("apple")
    assert game.is_won is True

def test_game_is_over_after_six_failed_guesses():
    game = Game("apple", ["apple", "brain", "chair", "cloud", "dance", "earth", "flame"])
    game.make_guess("brain")
    game.make_guess("chair")
    game.make_guess("cloud")
    game.make_guess("dance")
    game.make_guess("earth")
    game.make_guess("flame")
    assert game.is_over is True