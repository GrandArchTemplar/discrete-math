k = int(input())
arr = ['a', 'b', 'c', 'd', 'e']
res = ''
for i in range (2**k):
  s = input().split()
  if s[k] == '1':
    for j in range(k):
      if s[j] == '1':
        res += arr[j]
      else:
        res += '(' + '-' + arr[j] + ')'
      res += '^'
  res = res.rstrip('^').rstrip('+') + '+'
print(res.strip('+'))
