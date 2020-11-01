from enum import Enum


class expression_types(Enum):
    member = 1
    operand = 2
class expression_info:
    def __init__(self):
        self.left = None
        self.right = None
        self.expr_type = expression_types.member
        self.op = None

class field_info:
    def __init__(self):
        self.name = ""
        self.table = ""
        self.alias = ""
        self.table_alias = ""
        self.expr = expression_info()
    def __add__(self, other):
        pass

    def __repr__(self):
        return "[" + self.table_alias + "].[" + self.name + "]"


def db_field(*args, **kwargs):
    field_name = args[0]

    def ret_fn(*args, **kwargs):
        ret = field_info()
        ret.name = field_name
        return ret

    return ret_fn


def db_table(*args):
    __table_name__ = args[0]

    def ret_fn(*args):
        ret = args[0]()
        ret.__table_name__ = __table_name__
        for k, v in ret.__class__.__dict__.items():
            if isinstance(v, field_info):
                v.table = ret.__table_name__
                v.alias = v.name
                v.table_alias = v.table
                v.expr.expr_type
                ret.__dict__[k] = v
        return ret

    return ret_fn


@db_table("hr_emps")
class employees:
    @db_field("Code")
    def code(self): pass

    @db_field("FirstName")
    def name(self): pass


m = employees.code+" "+employees.code
print(m)
