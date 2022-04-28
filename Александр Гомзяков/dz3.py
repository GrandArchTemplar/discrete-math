b = input()
from itertools import chain, combinations
def powerset(list_name):
    s = list(list_name)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1))

A = set(map(int, input().split()))
print([])
for x in powerset(A):
    print(*x)

