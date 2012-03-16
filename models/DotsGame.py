import cfg

from models.Edge import VerticalEdge, HorizontalEdge, Square

class DotsGame:
    def __init__(self, edge_rows, edge_cols, squares):
        self.edge_rows = edge_rows
        self.edge_cols = edge_cols
        self.squares = squares

    def activate_edge(self, edge_x, edge_y, orientation):
        if orientation == 'horizontal':
            edge_matrix = self.edge_rows
        else:
            edge_matrix = self.edge_cols

        edge_matrix[edge_x][edge_y].activate()

    def print_board(self):
        for row in xrange(cfg.game_rows-1):
            for col in xrange(cfg.game_cols-1):
                print self.squares[col][row].repr_num(),
            print '\n'

def generate_matrix(obj, rows, cols):
    obj_matrix = []
    for count in xrange(rows):
        obj_row = []
        for count in xrange(cols):
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
    game.activate_edge(1,0,'vertical')
    game.print_board()
    return game
