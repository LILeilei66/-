
class Basic_Tree():
    def __init__(self, root=None):
        self.root = root
        self.left_children = None
        self.right_children = None

    def insert_left(self, item):
        self.left_children = Basic_Tree(item)

    def insert_right(self, item):
        self.right_children = Basic_Tree(item)

class ID3_Tree():
    def __init__(self, A, D, epsi):
        """

        :param A: Feature set
        :param D: Dataset
        """
        self.A = A
        self.D = D
        self.epsi = epsi

    def init_tree(self):
        if len(self.D['Label']) == 1:
            self.T = Basic_Tree(self.D['Label'][0])
        elif self.A == None:
            self.T = Basic_Tree(self.D['Label'][0])



    def _info_gain(self):
