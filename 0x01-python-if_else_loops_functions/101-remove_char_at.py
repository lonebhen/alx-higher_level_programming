#!/usr/bin/python3

def remove_char_at(str, n):
    final = ''

    for i in str:
        if i == str[n]:
            continue
        else:
            final += i

    return final


# print(remove_char_at("Slim Shady", 4))
