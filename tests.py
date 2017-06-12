import bowling
import pytest


@pytest.fixture()
def game():
    return bowling.Game()


def _roll_many(game, num_rolls, pins):
    for ii in range(num_rolls):
        game.roll(pins)


def _roll_spare(game):
    game.roll(5)
    game.roll(5)


def _roll_strike(game):
    game.roll(10)  # strike.


def test_gutter_game(game):
    _roll_many(game, 20, 0)
    assert game.score() == 0


def test_all_ones(game):
    _roll_many(game, 20, 1)
    assert game.score() == 20


def test_one_spare(game):
    _roll_spare(game)
    game.roll(4)
    _roll_many(game, 17, 0)
    assert game.score() == 18


def test_one_strike(game):
    _roll_strike(game)
    game.roll(3)
    game.roll(4)
    _roll_many(game, 16, 0)
    assert game.score() == 24


def test_perfect_game(game):
    _roll_many(game, 12, 10)
    assert game.score() == 300

