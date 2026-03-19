"""Player 模块单元测试"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.player import Player
from src.config import PLAYER_SPEED, JUMP_FORCE, GRAVITY


def make_player() -> Player:
    return Player(x=0, y=0, speed=PLAYER_SPEED, jump_force=JUMP_FORCE)


def test_initial_state():
    p = make_player()
    assert p.x == 0
    assert p.y == 0
    assert p.velocity_x == 0.0
    assert p.velocity_y == 0.0
    assert p.on_ground is False
    assert p.health == 100
    assert p.score == 0
    assert p.is_alive is True


def test_move_left():
    p = make_player()
    p.move_left()
    assert p.velocity_x == -PLAYER_SPEED


def test_move_right():
    p = make_player()
    p.move_right()
    assert p.velocity_x == PLAYER_SPEED


def test_stop():
    p = make_player()
    p.move_right()
    p.stop()
    assert p.velocity_x == 0.0


def test_jump_on_ground():
    p = make_player()
    p.on_ground = True
    p.jump()
    assert p.velocity_y == JUMP_FORCE
    assert p.on_ground is False


def test_jump_in_air():
    p = make_player()
    p.on_ground = False
    p.jump()
    assert p.velocity_y == 0.0


def test_apply_gravity():
    p = make_player()
    p.on_ground = False
    p.apply_gravity(GRAVITY)
    assert p.velocity_y == GRAVITY


def test_gravity_on_ground():
    p = make_player()
    p.on_ground = True
    p.apply_gravity(GRAVITY)
    assert p.velocity_y == 0.0


def test_update_position():
    p = make_player()
    p.velocity_x = 3.0
    p.velocity_y = 2.0
    p.update()
    assert p.x == 3.0
    assert p.y == 2.0


def test_collect_gem():
    p = make_player()
    p.collect_gem(10)
    assert p.score == 10
    p.collect_gem(20)
    assert p.score == 30


def test_take_damage():
    p = make_player()
    p.take_damage(40)
    assert p.health == 60
    assert p.is_alive is True


def test_lethal_damage():
    p = make_player()
    p.take_damage(200)
    assert p.health == 0
    assert p.is_alive is False
