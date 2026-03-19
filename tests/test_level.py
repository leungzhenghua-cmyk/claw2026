"""Level 模块单元测试"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.level import Level, Tile
from src.config import TILE_SIZE


def make_level() -> Level:
    return Level(width=10, height=10, tile_size=TILE_SIZE)


def test_initial_state():
    level = make_level()
    assert level.width == 10
    assert level.height == 10
    assert level.tile_size == TILE_SIZE
    assert level.tiles == []
    assert level.gems == []
    assert level.gem_count == 0


def test_add_tile():
    level = make_level()
    level.add_tile(0, 0)
    assert len(level.tiles) == 1
    assert level.tiles[0].x == 0
    assert level.tiles[0].y == 0
    assert level.tiles[0].solid is True


def test_add_non_solid_tile():
    level = make_level()
    level.add_tile(0, 0, solid=False)
    assert level.tiles[0].solid is False


def test_add_gem():
    level = make_level()
    level.add_gem(64, 64)
    assert level.gem_count == 1
    assert level.gems[0] == (64, 64)


def test_set_spawn():
    level = make_level()
    level.set_spawn(100, 200)
    assert level.spawn_x == 100
    assert level.spawn_y == 200


def test_get_solid_tiles():
    level = make_level()
    level.add_tile(0, 0, solid=True)
    level.add_tile(32, 0, solid=False)
    level.add_tile(64, 0, solid=True)
    solid = level.get_solid_tiles()
    assert len(solid) == 2
    assert all(t.solid for t in solid)
