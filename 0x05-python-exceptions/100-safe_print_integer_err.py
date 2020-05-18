def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return(True)
    except Exception as error_msn:
        sys.stderr.write("Exception: {}\n".format(error_msn))
        return(False)
