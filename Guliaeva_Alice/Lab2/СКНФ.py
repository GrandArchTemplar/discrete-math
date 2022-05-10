a=int(input())
mas = []
for i in range(2**a):
    mas.append(list(map(int, input().split())))
for i in range(2**a):
    if mas[i][a]==0:
        print("(", end="")
        for k in range(a):
           if mas[i][k]==1:
              print('-',end="")
           print(chr(ord('a')+k),end="")
           if k<a-1:
               print("+",end="")
        if i==2**a-1:
           print(")",end="")
        else:
            print(")^",end="")