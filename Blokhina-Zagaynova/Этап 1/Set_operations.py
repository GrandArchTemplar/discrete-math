def uniter (x, y): #объединятор
    return x.union(y)

def intersecter(x, y): #пересекатор
    return x.intersection(y)

def differencer(x, y): #вычитатор
    return x.difference(y)

def adder(x, y): #дополнятор
    return y.difference(x)
trash = input()
a = set(input().split())
b = set(input().split())
op = input()
if op in ['u', 'p', 's', 'a', 'i', '-']:
    if op == 'u':
        ans = uniter(a, b)
    elif op == 'p' or op == 'i':
        ans = intersecter(a, b)
    elif op == 's' or op == '-':
        ans = differencer(a, b)
    elif op == 'a':
        ans = adder(a, b)
    print(*sorted(ans))
else:
    print('Операция не найдена, попробуйте снова')