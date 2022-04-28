def subsets(A, N):
    sets = []
    for i in range(2 ** N):
        subset = []
        for j in range(N):
            if i & (2 ** j):
                subset.append(A[j])
        sets.append(subset)
    return sets

size = int(input())
set = list(map(int, input().split()))
if size == len(set):
    for i in subsets(set, size):
        print(i)