def prompt(out='', condition=lambda x: True, err='', transform=lambda x: x):
    while True:
        print(out, end='')
        inp = input()
        if condition(inp):
            return transform(inp)
        else:
            print(err, end='')

def canBe(val, type):
    if isinstance(val, type):
        return True
    try:
        type(val)
    except ValueError:
        return False
    return True

def root(base, index=2):
    return base ** (1 / index)
