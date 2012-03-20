import cfg

from models.Edge import VerticalEdge, HorizontalEdge, Square
from lib.ai import RandomAI

class DotsGame:
    def __init__(self, edge_rows, edge_cols, squares):
        self.edge_rows = edge_rows
        self.edge_cols = edge_cols
        self.squares = squares

    def is_edge_active(self, edge_x, edge_y, orientation):
        if orientation == 'horizontal':
            edge_matrix = self.edge_rows
        else:
            edge_matrix = self.edge_cols

        return edge_matrix[edge_x][edge_y].is_active
    
    def activate_edge(self, edge_x, edge_y, orientation):
        if orientation == 'horizontal':
            edge = self.edge_rows[edge_x][edge_y] 
            coords = []
            adj_boxes = {'top_box': -1, 'bottom_box': 0}
            for box_name, box_y in adj_boxes.items():
                box = getattr(edge, box_name)
                if box is not None and box.is_complete():
                    coords.append(edge_x, edge_y + box_y)
            return coords
        else:
            edge = self.edge_rows[edge_x][edge_y] 
            coords = []
            adj_boxes = {'left_box': -1, 'right_box': 0}
            for box_name, box_x in adj_boxes.items():
                box = getattr(edge, box_name)
                if box is not None and box.is_complete():
                    coords.append(edge_x + box_x, edge_y)
            return coords


    def print_board(self):
        for row in xrange(cfg.game_rows-1):
            for col in xrange(cfg.game_cols-1):
                print self.squares[col][row].repr_num(),
            print '\n'

    def print_ownership(self):
        pass

def generate_matrix(obj, rows, cols):
    obj_matrix = []
    for row_count in xrange(rows):
        obj_row = []
        for col_count in xrange(cols):
            obj_row.append(obj())
        obj_matrix.append(obj_row)
    return obj_matrix


def link_squares(edge_rows, edge_cols, squares):
    for row in xrange(cfg.game_rows-1):
        for col in xrange(cfg.game_cols-1):
            squares[col][row].link_edges(
                left_edge=edge_cols[col][row],
                right_edge=edge_cols[col+1][row],
                top_edge=edge_rows[col][row],
                bottom_edge=edge_rows[col][row+1],
            )

def create_new_game():
    edge_rows = generate_matrix(VerticalEdge, cfg.game_rows-1, cfg.game_cols)
    edge_cols = generate_matrix(HorizontalEdge, cfg.game_rows, cfg.game_cols-1)
    squares = generate_matrix(Square, cfg.game_rows-1, cfg.game_cols-1)
    link_squares(edge_rows, edge_cols, squares)
    game = DotsGame(edge_rows, edge_cols, squares)
    RandomAI(game).generate_move()
    game.print_board()
    return game
