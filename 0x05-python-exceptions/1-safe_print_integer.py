#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        print()
        return True
    except ValueError:
        return False


# value = "School"
# has_been_print = safe_print_integer(value)
# if not has_been_print:
#     print("{} is not an integer".format(value))
