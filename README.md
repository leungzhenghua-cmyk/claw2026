# claw2026

claw2026 openclaw 使用示例项目。

## 项目结构

```
claw2026/
├── src/
│   ├── __init__.py
│   ├── config.py    # 全局配置常量
│   ├── player.py    # 玩家角色逻辑
│   ├── level.py     # 关卡与砖块逻辑
│   └── game.py      # 游戏主循环与工厂函数
├── tests/
│   ├── test_player.py
│   ├── test_level.py
│   └── test_game.py
├── requirements.txt
└── README.md
```

## 快速开始

```bash
pip install -r requirements.txt
python -m src.game
```

## 运行测试

```bash
pip install pytest
pytest tests/ -v
```
