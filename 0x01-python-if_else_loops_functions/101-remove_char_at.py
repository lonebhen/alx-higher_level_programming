#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])


# print(remove_char_at("Slim Shady", 4))
# print(remove_char_at("Python", -2))
# print(remove_char_at("Chicago", 15))
