"""Game 模块单元测试"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.game import Game, create_default_level
from src.config import WINDOW_HEIGHT


def test_game_initial_state():
    game = Game()
    assert game.running is False
    assert game.current_level is None
    assert game.player is None
    assert game.frame == 0


def test_load_level():
    game = Game()
    level = create_default_level()
    level.set_spawn(50, 100)
    game.load_level(level)
    assert game.current_level is level
    assert game.player is not None
    assert game.player.x == 50
    assert game.player.y == 100


def test_start_stop():
    game = Game()
    game.start()
    assert game.running is True
    game.stop()
    assert game.running is False


def test_update_increments_frame():
    game = Game()
    level = create_default_level()
    game.load_level(level)
    game.update()
    assert game.frame == 1
    game.update()
    assert game.frame == 2


def test_update_without_level():
    game = Game()
    game.update()
    assert game.frame == 0


def test_create_default_level():
    level = create_default_level()
    assert level.width == 25
    assert level.height == 20
    assert level.gem_count == 3
    assert len(level.get_solid_tiles()) > 0
