from Task2 import *
from Task1 import *
from Task3 import *
from Task4 import *
def SetRun():
    array_A = set(input("Введите через пробел элементы множества 1: ").split(" "))

    array_B = set(input("Введите через пробел элементы множества 2: ").split(" "))


    print("u : объединение множеств \n"
          "i : пересечение множеств \n"
          "s : разность множеств 1-2 \n"
          "s- : симметрическая разность множеств \n"
          "a : дополнение множества 1 до множества 2 \n"
          "b - булеан множества 1")
    operation = input()

    if operation == "u":
        print(*sets_union(array_A, array_B))
    if operation == "i":
        print(*intersection(array_A, array_B))
    if operation == "s":
        print(*difference(array_A, array_B))
    if operation == "s-":
        print(*symmetric_difference(array_A, array_B))
    if operation == "a":
        print(*addition(array_A, array_B))
    if operation == "b":
        print(boolean(array_A))

if __name__ == "__main__":
    #SetRun() #множества
    #Graph()  #свойства графа
    #encode_string()    #кодирование строки
