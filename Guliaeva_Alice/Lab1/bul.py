def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
boolean = set()
x=int(input())
multiplicity = set()
mnoj=list(input().split())
for i in mnoj:
    multiplicity.add(int(i))
for r in range(len(multiplicity) + 1):
    temp = set(combinations(multiplicity, r))
    for i in temp:
        boolean.add(i)
a=sorted(boolean,key=sum)
for i in a:
    if i ==():
        print('[]')
        continue
    for j in range(len(i)):
        print(i[j],end=' ')
    print()