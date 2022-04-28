# Написать генератор булеанов данного числового множества
from itertools import combinations

a = int(input())
A = set(map(int, input().split()))
if a == len(A):
    for i in range(len(A) + 1):
        print([j for j in combinations(A, i)])
else:
    print('Ошибка в вводе количества элементов множетсва')

