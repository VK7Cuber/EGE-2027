# Кластеризация звёздного неба
# Пример решения задачи №31371 с kompege.ru

def get_distance(A, B):
    """
    Функция для получения расстояния между двумя точками (звёздами)
    :param A: координаты точки A
    :param B: координаты точки B
    :return: расстояние между ними
    """
    x1, y1 = A
    x2, y2 = B
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


file = open("27_A_31371.txt")

klaster_1 = []
klaster_2 = []
blue_starts_1 = []
blue_starts_2 = []

for st in file: # Разделение точек по кластерам
    x, y, start_type = st.replace(",", ".").split(" ") # Python воспринимает дробные числа только с точкой, поэтому
                                                                    # заменяем запятые на точки и разбиваем на переменные
    x, y = float(x), float(y)
    start_type = start_type.strip() # На всякий случай, так как в конце строки могут быть "\n", которые ломают условие
                                    # для выборки звёзд
    if y < 6: # Граница разделения кластеров - 6, её узнаём из визуализации в электронной таблице!
        klaster_1.append((x, y))
        if start_type[0] == "O" and start_type[-2:] == "VI": # если звезда по типу подходит нашему условию
            blue_starts_1.append((x, y))
    else:
        klaster_2.append((x, y))
        if start_type[0] == "O" and start_type[-2:] == "VI": # ВАЖНО!!! Не путаем букву "O" и число 0!
            blue_starts_2.append((x, y))

klaster_center = (0, 0) # ищем центр кластера - точку, от которой сумма расстояний до всех других точек будет наименьшей
min_distance = 10**10
for A in klaster_1: # для начала для первого кластера
    sum_distance = 0 # сумма расстояний до каждой звезды
    for B in klaster_1:
        sum_distance += get_distance(A, B) # прибавляем к сумме новое расстояние
    if sum_distance < min_distance:
        min_distance = sum_distance
        klaster_center = A

print(klaster_center) # -> (4.8167, 5.06735)
center_1 = klaster_center # координаты центра первого кластера

klaster_center = (0, 0)
min_distance = 10**10
for A in klaster_2: # потом точно такая же операция для второго кластера
    sum_distance = 0
    for B in klaster_2:
        sum_distance += get_distance(A, B)
    if sum_distance < min_distance:
        min_distance = sum_distance
        klaster_center = A

print(klaster_center) # -> (4.51545, 7.0512)
center_2 = klaster_center # координаты центра второго кластера

print(get_distance(center_1, center_2) * 10_000) # ответ на первый вопрос - расстояние между центрами двух кластеров

min_star_distance = 10**10 # ищем минимальное расстояние между двумя звёздами в двух кластерах
for A in blue_starts_1: # подходящие по условию звёзды из первого кластера
    for B in blue_starts_2: # подходящие по условию звёзды из второго кластера
        min_star_distance = min(get_distance(A, B), min_star_distance)
print(min_star_distance) # ответ на второй вопрос: минимальное расстояние между двумя голубыми субкарликами