#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except ValueError:
            continue
        except TypeError:
            continue
    print("")
    return count


# my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
# # nb_print = safe_print_list_integers(my_list, len(my_list))
# nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
# print(nb_print)
