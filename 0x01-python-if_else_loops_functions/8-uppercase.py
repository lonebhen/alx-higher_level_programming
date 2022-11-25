#!/usr/bin/python3

def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            letter = 32
        else:
            letter = 0
        print("{:c}".format(ord(str[i]) - letter), end='')
    print()


# uppercase("Best")
# uppercase("Hello Slim")
