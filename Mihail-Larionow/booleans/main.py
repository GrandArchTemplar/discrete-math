import itertools as it

if __name__ == '__main__':
    a = input()
    A = set(input())
    A.discard(' ')
    print([])
    for i in range(1, len(A)+1):
        subsets = list(it.combinations(A, i))
        for subset in subsets:
            for element in subset:
                print(element, end=' ')
            print()
