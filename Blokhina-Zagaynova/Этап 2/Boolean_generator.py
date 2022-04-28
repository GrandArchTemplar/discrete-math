def subsets(a, n):
    sets = []
    for i in range(2**n):
        subset=[]
        for mask in range(n):
            if i & (2**mask):
                subset.append(a[mask])
        sets.append(subset)
    return sets

size = int(input())
set = list(map(int, input().split()))
if size == len(set):
    for i in subsets(set, size):
        print(i)
else:
    print('Длина множества указана неверно, попробуйте снова')