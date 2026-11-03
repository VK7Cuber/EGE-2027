# Графы
# Ацикличные графы - графы, в которых, выйдя из одной вершины, невозможно попасть в другую

# 1. Алгоритм Дейкстры (полный)
# ------------------------
file = open("23.txt")

vertex = set() # множество вершин
weight_dict = {} # словарь с весами ребёр. Структура: {(f, t): m}
                 # f - откуда, t - куда, m - вес

for line in file: # заполняем наши коллекции
    from_, to_, w = map(float, line.split())
    vertex.add(from_)
    vertex.add(to_)
    weight_dict[(from_, to_)] = w

# Словарь минимальных расстояний:
min_distance = dict.fromkeys(vertex, 10**10) # заполняем словарь min_distance ключами из vertex со значениями 10**10
# выглядит так: {1.0: 10000000000, 4.0: 10000000000, 262.0: 10000000000, 390.0: 10000000000, ......}
current_vertex = 1 # в этой переменной храним номер вершины, в которой мы находимся.
min_distance[current_vertex] = 0 # из первой вершины в первую длина 0

# Тут может быть ещё строчка, в которой мы убираем вершину (вершины), через которую нам НЕ НУЖНО проходить (по условию)
# vertex -= {663, 173}

while vertex: # пока список вершин не опустеет
    minimum = 10 ** 10 # переменная для поиска минимального значения
    for element in vertex:
        if min_distance[element] < minimum: 
            minimum = min_distance[element]
            current_vertex = element
    if minimum == 10 ** 10: break
    vertex -= {current_vertex}
    for el in vertex:
        if (current_vertex, el) in weight_dict:
            min_distance[el] = min(min_distance[el], min_distance[current_vertex] + weight_dict[(current_vertex, el)])
print(min_distance[100]) # ключ - номер вершины, до какой идём
