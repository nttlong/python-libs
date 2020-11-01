from .fields import field

class field_member(field):

    def __init__(self, table_name, field_name):
        self.name = field_name
        self.table = table_name
        self.alias = field_name
        self.table_alias = table_name
    def __repr__(self):
        return "[" + self.table_alias +"].[" +self.name +"]"