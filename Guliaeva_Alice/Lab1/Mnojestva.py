def u(a,b):
    return(a.union(b))
def i(a,b):
    return(a.intersection(b))

def s(a, b):
    return (a.difference(b))
def a(a,b):
    return(b.difference(a))
x=input()
set1 = set(input().split())
set2 = set(input().split())
op=input()
if op == "u":
    print(sorted(u(set1, set2)))
elif op == "i":
    print(sorted(i(set1, set2)))
elif op == "s":
    print(sorted(s(set1, set2)))
elif op == "a":
    print(sorted(a(set1, set2)))
else:
    print("Такой операции нет")


