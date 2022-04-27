vars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
k = int(input())
s = [list(map(int, input().split())) for i in range(pow(2, k))]
for i in range(len(s)):
    for j in range(len(s[j]) - 1):
        if s[i][j] == 0:
            s[i][j] = f'(-{vars[j]})'
        else:
            s[i][j] = vars[j]
    if s[i][k] == 1:
        del s[i][k]
        for j in range(len(s[i])):
            if j < len(s[i]) - 1:
                print(s[i][j], end="^")
            elif i < len(s) - 1:
                print(s[i][j], end='+')
            else:
                print(s[i][j])
