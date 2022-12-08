#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
    except TypeError:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False


# value = "School"
# has_been_print = safe_print_integer_err(value)
# if not has_been_print:
#     print("{} is not an integer".format(value))
