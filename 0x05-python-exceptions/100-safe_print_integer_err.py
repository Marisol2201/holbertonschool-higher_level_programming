def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return(True)
    except Exception as error_msn:
        print("Exception: {}".format(error_msn), file=sys.stderr)
        return(False)
