# Операции с множествами A и B
# объединятор(u), пересекатор(i или p), вычитатор(s или -) и дополнятор(a)
a, b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
operation = input()
if (a == len(A)) and (b == len(B)):
    if operation == 'u':
        print(A.union(B))
    elif operation == 'i' or operation == 'p':
        print(A.intersection(B))
    elif operation == 's' or operation == '-':
        print(A.difference(B))
    elif operation == 'a':
        print(B.difference(A))
    else:
        print('Операции не существует')
else:
    print('Ошибка в вводе количества элементов множетсва')


