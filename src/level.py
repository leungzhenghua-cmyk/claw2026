"""关卡模块"""

from typing import List, Tuple


class Tile:
    """地图砖块。"""

    def __init__(self, x: int, y: int, solid: bool = True):
        self.x = x
        self.y = y
        self.solid = solid


class Level:
    """游戏关卡，包含砖块地图和出生点。"""

    def __init__(self, width: int, height: int, tile_size: int = 32):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.tiles: List[Tile] = []
        self.spawn_x = 0
        self.spawn_y = 0
        self.gems: List[Tuple[int, int]] = []

    def add_tile(self, x: int, y: int, solid: bool = True):
        """添加砖块到关卡。"""
        self.tiles.append(Tile(x, y, solid))

    def add_gem(self, x: int, y: int):
        """在指定位置添加宝石。"""
        self.gems.append((x, y))

    def set_spawn(self, x: int, y: int):
        """设置玩家出生点。"""
        self.spawn_x = x
        self.spawn_y = y

    def get_solid_tiles(self) -> List[Tile]:
        """获取所有实体砖块。"""
        return [tile for tile in self.tiles if tile.solid]

    @property
    def gem_count(self) -> int:
        """关卡中宝石的数量。"""
        return len(self.gems)
