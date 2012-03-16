class Edge:
    def __init__(self):
        self.is_active = False

    def activate(self):
        self.is_active = True

class VerticalEdge(Edge):
    def __init__(self, left=None, right=None):
        self.left_box = left
        self.right_box = right
        Edge.__init__(self)

class HorizontalEdge(Edge):
    def __init__(self, top=None, bottom=None):
        self.top_box = top
        self.bottom_box = bottom
        Edge.__init__(self)

class Square:
    def link_edges(self, left_edge, right_edge, top_edge, bottom_edge):
        self.left_edge = left_edge # trust me, this links everything
        left_edge.right_box = self
        self.right_edge = right_edge
        right_edge.left_box = self
        self.top_edge = top_edge
        top_edge.bottom_box = self
        self.bottom_edge = bottom_edge
        bottom_edge.top_box = self
