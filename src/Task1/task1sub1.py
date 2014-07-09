from sys import argv


def add_num():
    script, a, b = argv
    a = int(a)
    b = int(b)
    print (a + b) * (abs(b - a) + 1) / 2

add_num()