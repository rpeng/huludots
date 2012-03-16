class Edge():
    pass

class VerticalEdge(Edge):
    def __init__(self, left=None, right=None):
        self.left_box = left
        self.right_box = right

class HorizontalEdge(Edge):
    def __init__(self, top=None, bottom=None):
        self.top_box = top
        self.bottom_box = bottom
