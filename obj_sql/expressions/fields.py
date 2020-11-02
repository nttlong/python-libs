

class field(object):

    def __init__(self):
        pass

    def __add__(self, other):

        from .fields_expression import field_expression
        from .fields_value import field_value

        ret = field_expression()
        ret.left = self
        ret.op = "+"
        if isinstance(other,field):
            ret.right = other
        else:
            ret.right = field_value(other)

        return ret

    def __sub__(self, other):

        from .fields_expression import field_expression
        from .fields_value import field_value

        ret = field_expression()
        ret.left = self
        ret.op = "-"
        if isinstance(other, field):
            ret.right = other
        else:
            ret.right = field_value(other)

        return ret

    def __eq__(self, other):
        from .fields_expression import field_expression
        ret = field_expression()
        ret.left = self
        ret.op = "=="
        ret.right = other
        return ret