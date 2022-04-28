def sets_union(array1, array2):
    result_set = array1.union(array2)
    result_set = sorted(result_set)
    return result_set


# пересечение множеств
def intersection(array1, array2):
    result_set = array1 & array2
    result_set = sorted(result_set)
    return result_set


# разность множеств
def difference(array1, array2):
    result_set = array1 - array2
    result_set = sorted(result_set)
    return result_set


# симметричная разность
def symmetric_difference(array1, array2):
    result_set = array1 ^ array2
    result_set = sorted(result_set)
    return result_set


# массив 1 дополняется до массива 2
def addition(array1, array2):
    result_set = array2 - array1
    result_set = sorted(result_set)
    return result_set