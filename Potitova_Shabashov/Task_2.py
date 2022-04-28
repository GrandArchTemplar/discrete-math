def subsets(S):
    sets = []
    for i in range(1 << n):
        subset = [int(S[bit]) for bit in range(n) if i & (1 << bit)]
        sets.append(subset)
    return sets

n = int(input())
S = input()
S = S.split()
for m in subsets(S):
    print(m)