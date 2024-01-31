class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game) -> None:
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()
        # 游戏刚启动时处于活动状态
        self.game_active = False
        # 任何情况下都不应重置最高得分
        self._read_high_score()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _read_high_score(self): 
        with open(self.settings.high_score_file) as file_object:
            read_high_score = file_object.read()
            if len(read_high_score) == 0 or read_high_score.isspace():
                self.high_score = 0
            else:
                self.high_score = int(read_high_score)