from functools import lru_cache # Чтобы рекурсивная функция не выполнялась слишком долго,
                                # используем кэш
file = open("23.txt")

d = [[] for _ in range(1001)]
for string in file:
    s = string.strip().split()
    from_, to_ = int(s[0]), int(s[1])
    d[from_].append([to_, float(s[2])])

@lru_cache(None)
def getMinDist(x, y):
    """
    Рекурсивная функция для поиска кратчайшего пути в графе
    :param x: вершина, из которой идём
    :param y: вершина, в которую идём
    :return:
    """
    if x == y: return 0
    if len(d[x]) == 0 or x == "исключенная вершина": return 10**10 # кратчайший путь, не проходящий через определенную вершину
    return min(w + getMinDist(k, y) for k, w in d[x])

print(getMinDist(1, 100)) # просто кратчайший путь
print(getMinDist(1, 44) + getMinDist(44, 100)) # кратчайший путь, проходящий через определенную вершину