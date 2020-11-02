from .fields import field


class field_member(field):

    def __init__(self, table_name, field_name):
        self.name = field_name
        self.table = table_name
        self.alias = field_name
        self.table_alias = table_name

    def __str__(self):
        from .utils import __create_text__
        return __create_text__(self.table_alias , self.name )

