def challenge_1():
    for i in range(5):
        print("*" * (i + 1))
    print()


def challenge_2():
    for i in range(5):
        print("*" * (5 - i))
    print()


def challenge_3():
    for i in range(5):
        print((" " * (5 - i)) + ("*" * (i + 1)))
    print()


def challenge_4():
    for i in range(5):
        print((" " * (i + 1)) + ("*" * (5 - i)))
    print()


def challenge_5():
    for i in range(5):
        print((" " * (5 - i)) + ("*" * (2 * i + 1)))
    print()


# challenge_1()
# challenge_2()
# challenge_3()
# challenge_4()
challenge_5()
