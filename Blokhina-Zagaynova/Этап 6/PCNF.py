arr=['a','b','c','d','e']
k=int(input())
res=''
for i in range(2**k):
  x=input().split()
  if x[k]=='0':
      res+='('
      for j in range(len(x)-1):
        if j<k and j>0:
          res+=' + '
        if x[j]=='0':
          res+=arr[j]
        else:
          res+='-'+arr[j]
      res+=')'
print(res)