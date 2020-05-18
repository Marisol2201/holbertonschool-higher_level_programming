import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return(True)
    except (ValueError) as error_msn:
        print("Exception: {}".format(error_msn), file=sys.stderr)
        return(False)
