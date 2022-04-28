def sim(graf):
    pr=0
    for i in graf:
        if (i[1],i[0]) in graf:
            pr+=1
    if pr==len(graf):
        print('Симметрично')
    elif pr==0:
        print('Антисимметрично')
    else:
        print('Несимметрично')
def ref(graf,a):
    pr=0
    for i in graf:
        if i[0]==i[1]:
            pr+=1
    if pr==a:
        print('Рефлексивно')
    elif pr==0:
        print('Антирефлексивно')
    else:
        print('Нерефлексивно')
def trans(graf):
    pr=0
    y=0
    for i in graf:
        for j in graf:
            if i[1]==j[0]:
                y+=1
                if (i[1],j[0]) in graf:
                    pr+=1
    if pr==y:
        print('Транзитивно')
    elif pr==0 and y!=0:
        print('Антитранзитивно')
    else:
        print('Нетранзитивно')
x=list(input().split())
a=int(x[0])
b=int(x[1])
c = set()
for i in range(b):
    x=list(input().split())
    c.add(tuple(x))
sim(c)
ref(c,a)
trans(c)
