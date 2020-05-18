def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}".format(value))
        return(True)
    except Exception as error_msn:
        stderr.write("Exception: {}\n".format(error_msn))
        return(False)
