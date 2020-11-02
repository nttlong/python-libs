def __create_text__(*args, **kwargs):
    if isinstance(args, tuple):
        return '[' + args[0] + '].[' + args[1] + ']'
