"""玩家模块"""


class Player:
    """表示游戏中的玩家角色。"""

    def __init__(self, x: float, y: float, speed: float, jump_force: float):
        self.x = x
        self.y = y
        self.speed = speed
        self.jump_force = jump_force
        self.velocity_x = 0.0
        self.velocity_y = 0.0
        self.on_ground = False
        self.health = 100
        self.score = 0

    def move_left(self):
        """向左移动玩家。"""
        self.velocity_x = -self.speed

    def move_right(self):
        """向右移动玩家。"""
        self.velocity_x = self.speed

    def stop(self):
        """停止水平移动。"""
        self.velocity_x = 0.0

    def jump(self):
        """如果在地面上则跳跃。"""
        if self.on_ground:
            self.velocity_y = self.jump_force
            self.on_ground = False

    def apply_gravity(self, gravity: float):
        """应用重力。"""
        if not self.on_ground:
            self.velocity_y += gravity

    def update(self):
        """根据速度更新位置。"""
        self.x += self.velocity_x
        self.y += self.velocity_y

    def collect_gem(self, value: int = 10):
        """收集宝石并增加分数。"""
        self.score += value

    def take_damage(self, amount: int):
        """受到伤害。"""
        self.health = max(0, self.health - amount)

    @property
    def is_alive(self) -> bool:
        """玩家是否存活。"""
        return self.health > 0
