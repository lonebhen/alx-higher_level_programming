#!/usr/bin/python3

def safe_print_division(a, b):
    # result = 0

    try:
        result = a/b
    except ZeroDivisionError:
        result = None
    except ValueError:
        pass
    finally:
        print("Inside result: {}".format(result))
        print("{:d} / {:d} = {}".format(a, b, result))


# a = 0
# b = 2
# ans = safe_print_division(a, b)
