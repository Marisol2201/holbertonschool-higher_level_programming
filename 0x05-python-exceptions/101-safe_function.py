#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
        return result
    except Exception as excep:
        sys.stderr.write("Exception: {}\n".format(excep))
        return None
