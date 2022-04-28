def is_symmetrical(pairs):
    inverted_pairs = list()
    count = 0
    for pair in pairs:
        inverted_pairs.append([pair[1], pair[0]])
    for pair in inverted_pairs:
        if pair in pairs:
            count += 1
    if count == len(pairs):
        return "симметрично"
    elif count == 0:
        return "антисимметрично"
    else:
        return "ассимметрично"


def is_transitive(pairs):
    points_c = list()
    non_transitive = True
    full_transitive = True
    for pair in pairs:
        points_c.append(pair[1])
    for pair in pairs:
        for point_c in points_c:
            if [pair[1], point_c] in pairs and [pair[0], point_c] not in pairs:
                full_transitive = False
            elif [pair[1], point_c] in pairs and [pair[0], point_c] in pairs:
                non_transitive = False
    if not non_transitive:
        if full_transitive: return "транзитивно"
        else: return "нетранзитивно"
    else:
        return "антитранзитивно"


def is_reflexive(points, pairs):
    count = 0
    for point in points:
        if [point, point] in pairs:
            count += 1
    if count == len(points):
        return "рефлексивно"
    elif count == 0:
        return "антирефлексивно"
    else:
        return "нерефлексивно"


if __name__ == '__main__':
    n, k = map(int, input().split())
    pairs = list()
    points = list()
    for point in range(n):
        points.append(point)
    for rib in range(k):
        pairs.append(list(map(int, input().split())))
    print(is_symmetrical(pairs))
    print(is_transitive(pairs))
    print(is_reflexive(points, pairs))

