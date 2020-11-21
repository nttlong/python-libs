from sqlalchemy import Column as __column__

__locked__ = object()


def db_field(field_name):
    _field_name = field_name
    __locked__ = object()


def __create_column_from_type__(col_name, col_type) -> __column__:
    from datetime import datetime
    from sqlalchemy import Column, String, DateTime, Integer,Boolean
    if isinstance(col_type,tuple):
        ret_col= Column(col_name)
        for c_type in col_type:
            if type(c_type)==type:
                if c_type==str:
                    ret_col.type=String()
                elif c_type == int:
                    ret_col.type = Integer()
                elif c_type == bool:
                    ret_col.type = Boolean()
                else:
                    raise (Exception("It looks like The type " + str(col_type) + " of " + col_name + " is not support"))
            if isinstance(c_type, __alow_null__):
                ret_col.nullable = c_type.yes
            if isinstance(c_type,__size__):
                ret_col.type.length = c_type.__len__
        return ret_col
    elif isinstance(col_type,__size__):
        return Column(col_name, String(col_type.__len__))
    elif col_type == str:
        return Column(col_name, String)
    elif col_type == datetime:
        return Column(col_name, DateTime)
    elif col_type == int:
        return Column(col_name, Integer)
    elif col_type == bool:
        return Column(col_name, Boolean)
    else:
        raise (Exception("It looks like The type " + str(col_type) + " of "+col_name+" is not support"))


def db_table(table_name):
    _table_name = table_name

    def create_entity(entity):
        from sqlalchemy import Table, MetaData
        meta = MetaData()
        table_info = (_table_name, meta,)
        assert (issubclass(entity, object))
        for k, v in entity.__dict__.items():
            if k[0:2] != "__" and k[-2:] != "__":
                    col = __create_column_from_type__(k, v)
                    col.__doc__ = v.__doc__
                    col.comment = v.__doc__
                    if isinstance(entity.__keys__, list):
                        if k in entity.__keys__:
                            col.primary_key = True
                    table_info = table_info + (col,)
        db_tbl = Table(*table_info)

        return db_tbl

    return create_entity


def db_keys(keys):
    if not isinstance(keys, list):
        keys = [keys]
    _keys = keys

    def __keys__(entity):
        setattr(entity, "__keys__", _keys)
        return entity

    return __keys__


class __size__:
    def __init__(self,len):
        self.__len__ = len

class __alow_null__:
    def __init__(self, yes=True):
        self.yes=yes

class db_field:
    @staticmethod
    def size(len):
        return __size__(len)

    @staticmethod
    def allow_null(yes=True):
        return __alow_null__(yes)
