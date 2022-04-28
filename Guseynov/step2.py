import itertools
from itertools import combinations
class Set:
    def __init__(self, lst_of_items=None):
        self._list = []
        if lst_of_items is not None:
            for item in lst_of_items:
                self.add(item)

    def __str__(self):
        return str(" ".join(map(str, self._list)))

    def __iter__(self):
        return iter(self._list.copy())

    def __len__(self):
        return len(self._list)

    def add(self, item):
        if item not in self._list:
            self._list.append(item)

    def remove(self, item):
        self._list.remove(item)

    def union(set1, set2):
        return Set((set1._list + set2._list))

    def intersection(set1, set2):
        return Set([item for item in set2._list if item in set1._list])

    def difference(set1, set2):
        return Set([item for item in set1._list if item not in set2._list])

    def addiction(set1, set2):
        return Set.difference(set2, set1)

    def boolean(self):
        boolean = Set()
        for i in range(len(self) + 1):
            temp = list(itertools.combinations(self._list, i))
            for j in temp:
                boolean.add(j)
        return boolean



if __name__ == '__main__':
    print("	☆*:.｡.o(≧▽≦)o.｡.:*☆")
    n = input()
    set1 = Set(list(map(int, input().split())))
    set2 = Set(list(map(int, input().split())))
    operation = input()
    if operation == "u":
        print(Set.union(set1, set2))
    elif operation == "p":
        print(Set.intersection(set1, set2))
    elif operation == "-":
        print(Set.difference(set1, set2))
    elif operation == "a":
        print(Set.addiction(set1, set2))
    elif operation == "b": # boolean
        print(set1.boolean())
    else:
        print(">.<")
