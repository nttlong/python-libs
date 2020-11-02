def select(*args, **kwargs):
    from .expressions import field
    if isinstance(args, tuple):
        for v in args:
            if isinstance(v, field):
                pass
    pass
def join(*args,**kwargs):
    pass