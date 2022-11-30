#!/usr/bin/python3

def remove_char_at(str, n):
    final = ''

    while n >= 0:
        for i in str:
            if i == str[n]:
                continue
            else:
                final += i

        return final
    return str


# print(remove_char_at("Slim Shady", 4))
# print(remove_char_at("Python", -2))
