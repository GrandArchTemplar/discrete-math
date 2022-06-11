vars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
k = int(input())
s = [list(map(int, input().split())) for i in range(pow(2, k))]
result_lst = []
result = ''
for i in range(len(s)):
    for j in range(len(s[i]) - 1):
        if s[i][j] == 1:
            s[i][j] = f'-{vars[j]}'
        else:
            s[i][j] = vars[j]
    if s[i][k] == 0:
        del s[i][k]
        result_lst.append(s[i])
for i in range(len(result_lst)):
    result += '('
    for j in range(len(result_lst) - 1):
        result += result_lst[i][j] + ' + '
    result += result_lst[i][-1] + ')'
print(result)