class Edge:
    def __init__(self):
        self.is_active = False

    def activate(self):
        self.is_active = True
        return self.status()

class VerticalEdge(Edge):
    def __init__(self, left=None, right=None):
        self.left_box = left
        self.right_box = right
        Edge.__init__(self)

    def status(self):
        box_left = self.left_box
        box_right = self.right_box

class HorizontalEdge(Edge):
    def __init__(self, top=None, bottom=None):
        self.top_box = top
        self.bottom_box = bottom
        Edge.__init__(self)


class Square:

    def true_active(self, edge):
        if edge.is_active:
            return 1
        return 0

    def repr_num(self):
        num = self.true_active(self.top_edge)+\
                self.true_active(self.right_edge)*2+\
                self.true_active(self.bottom_edge)*4+\
                self.true_active(self.left_edge)*8
        return num

    def link_edges(self, left_edge, right_edge, top_edge, bottom_edge):
        self.left_edge = left_edge # trust me, this links everything
        left_edge.right_box = self
        self.right_edge = right_edge
        right_edge.left_box = self
        self.top_edge = top_edge
        top_edge.bottom_box = self
        self.bottom_edge = bottom_edge
        bottom_edge.top_box = self

    def is_complete(self):
        return self.left_edge.is_active and\
                self.right_edge.is_active and\
                self.bottom_edge.is_active and\
                self.top_edge.is_active

    def __init__(self):
        self.owner = None
