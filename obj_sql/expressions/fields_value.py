from .fields import field


class field_value(field):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "'" + self.value + "'"
