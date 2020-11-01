from .fields import field

class field_expression(field):

    def __init__(self):
        self.left = None
        self.right = None
        self.op = None
    def __repr__(self):
        return self.left + self.op + self.right
