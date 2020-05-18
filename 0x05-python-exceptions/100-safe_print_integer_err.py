def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return(True)
    except Exception as e:
        msn = "Exception: Unknown format code 'd' for object of type 'str'\n"
        sys.stderr.write(msn)
        return(False)
