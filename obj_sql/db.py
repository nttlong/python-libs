from . import expressions
exprs =expressions

def field(*args, **kwargs):
    field_name = args[0]

    def ret_fn(*args):
        ret = exprs.field_member("" , field_name)
        ret.name = field_name
        return ret

    return ret_fn


def table(*ags):
    __table_name__ = ags[0]

    def ret_fn(*args):
        from .expressions.tables import table

        ret = table()
        ret.name = __table_name__
        ret.alias = "T" + str(ret.__alias_index__)
        for k, v in args[0].__dict__.items():
            if isinstance(v, exprs.field_member):
                v.table = ret.name
                v.alias = v.name
                v.table_alias = ret.alias

                ret.__dict__[k] = v
        return ret

    return ret_fn
