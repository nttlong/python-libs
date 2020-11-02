from .fields import field


class field_expression(field):

    def __init__(self):
        self.left = None
        self.right = None
        self.op = None

    def __str__(self):
        return str(self.left) + self.op + str( self.right)

