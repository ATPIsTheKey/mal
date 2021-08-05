import sys


def READ(x):
    return x


def EVAL(x):
    return x


def PRINT(x):
    return x


def rep(x):
    print(x)
    return x


if __name__ == '__main__':
    try:
        while line := input("user> "):
            rep(line)
    except EOFError:
        exit(0)
