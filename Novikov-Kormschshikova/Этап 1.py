a = set(input().split(' '))
b = set(input().split(' '))
op = input()

if op == 'u':
    print(sorted(set.union(a, b)))
elif op == 'i':
    print(sorted(set.intersection(a, b)))
elif op == 's':
    print(sorted(a - b))
elif op == 'a':
    print(sorted(b - a))