import random

import cfg

class Move:
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation

    def to_dict(self):
        return {
            'x': self.x,
            'y': self.y,
            'orientation': self.orientation
        }

class RandomAI():
    def generate_move(self):
        while True:
            orientation = ['vertical','horizontal'][random.randrange(0,2)]
            x = random.randrange(0, cfg.game_cols-1)
            y = random.randrange(0, cfg.game_rows-1)
            print x, y, orientation
            if self.game.is_edge_active(x, y, orientation):
                continue
            else:
                self.game.activate_edge(x, y, orientation)
                break

    def __init__(self, game):
        self.game = game
