c, d = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
op = input()
if (c == len(a)) and (d == len(b)):
    if op == "u":
        print(a | b)
    elif op == "p":
        print(a & b)
    elif op == "-":
        print(a - b)
    elif op == "a":
        print(b.difference(a))
    else:
        print("Операция не выполнена")
else:
    print("Неверное количество данных")
