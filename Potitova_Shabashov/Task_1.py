# Два множества: A и B
# Операции: u - объединение, i или p - пересечение, - или s - вычитание, a - дополнение

n_a, n_b = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
if (len(a) != n_a) | (len(b) != n_b):
    print('Было заявлено другое количество элементов')
else:
    op = input()
    if op == 'u':
        print(a | b)
    elif (op == 'i') | (op == 'p'):
        print(a & b)
    elif (op == '-') | (op == 's'):
        print(a - b)
    elif op == 'a':
        if a <= b:
            print(b - a)
        else: print('Операция "дополнение" невозможна')
    else: print('Операция не определена')