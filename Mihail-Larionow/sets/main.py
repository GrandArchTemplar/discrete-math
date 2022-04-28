if __name__ == '__main__':
    A = {}; B = {}
    a = input()
    A = set(input())
    B = set(input())
    operation = input()
    print()
    A.discard(' ')
    B.discard(' ')
    my_switch = {
        "u": A | B,
        "p": A & B,
        "s": A - B,
        "a": (A | B) - A,
        "r": A ^ B
    }
    try:
        res = my_switch[operation]
    except KeyError as e:
        raise ValueError('Undefined unit: {}'.format(e.args[0]))
    for element in res:
        print(element, end=' ')
