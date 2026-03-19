"""游戏主模块"""

from src.config import (
    WINDOW_TITLE,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    FPS,
    PLAYER_SPEED,
    JUMP_FORCE,
    GRAVITY,
    TILE_SIZE,
)
from src.player import Player
from src.level import Level


class Game:
    """管理游戏主循环和状态。"""

    def __init__(self):
        self.running = False
        self.current_level: Level | None = None
        self.player: Player | None = None
        self.frame = 0

    def load_level(self, level: Level):
        """加载关卡并初始化玩家。"""
        self.current_level = level
        self.player = Player(
            x=level.spawn_x,
            y=level.spawn_y,
            speed=PLAYER_SPEED,
            jump_force=JUMP_FORCE,
        )

    def update(self):
        """更新一帧游戏逻辑。"""
        if self.player is None or self.current_level is None:
            return

        self.player.apply_gravity(GRAVITY)
        self.player.update()

        # 简单地面碰撞检测（y >= WINDOW_HEIGHT 时落地）
        if self.player.y >= WINDOW_HEIGHT:
            self.player.y = WINDOW_HEIGHT
            self.player.velocity_y = 0.0
            self.player.on_ground = True

        self.frame += 1

    def start(self):
        """标记游戏为运行状态。"""
        self.running = True

    def stop(self):
        """停止游戏。"""
        self.running = False


def create_default_level() -> Level:
    """创建默认演示关卡。"""
    level = Level(width=25, height=20, tile_size=TILE_SIZE)
    level.set_spawn(x=64, y=64)

    # 添加地板砖块
    for col in range(25):
        level.add_tile(x=col * TILE_SIZE, y=19 * TILE_SIZE)

    # 添加平台
    for col in range(5, 10):
        level.add_tile(x=col * TILE_SIZE, y=14 * TILE_SIZE)
    for col in range(14, 20):
        level.add_tile(x=col * TILE_SIZE, y=10 * TILE_SIZE)

    # 添加宝石
    level.add_gem(x=7 * TILE_SIZE, y=13 * TILE_SIZE)
    level.add_gem(x=16 * TILE_SIZE, y=9 * TILE_SIZE)
    level.add_gem(x=18 * TILE_SIZE, y=9 * TILE_SIZE)

    return level


def main():
    """程序入口。"""
    game = Game()
    level = create_default_level()
    game.load_level(level)
    game.start()
    print(f"{WINDOW_TITLE} 已启动 ({WINDOW_WIDTH}x{WINDOW_HEIGHT} @ {FPS}fps)")
    print(f"关卡大小: {level.width}x{level.height}, 宝石数量: {level.gem_count}")
    game.stop()


if __name__ == "__main__":
    main()
