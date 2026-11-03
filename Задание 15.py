# Задание 15
####### Тип 1
# https://education.yandex.ru/ege/inf/task/de253bda-d45a-4a92-a139-ba96506c8f57?clckid=dbfea5af
res = []
for A in range(1, 300):
    flg = True
    for x in range(0, 300):
        for y in range(0, 300):
            f = (x + 2 * y < A) or (y > x) or (x > 60)
            if f == 0:
                flg = False
    if flg == 1:
        res.append(A)
print(min(res))

####### Тип 2
# https://education.yandex.ru/ege/inf/task/b4197b61-d861-44bf-993e-e7f1b664376d?clckid=df75381c
res = []
for A in range(1, 300):
    flg = True
    for x in range(1, 300): # ПЕРЕБИРАЕМ ДО ПРОИЗВЕДЕНИЯ ВСЕХ ДАННЫХ В УСЛОВИИ ЧИСЕЛ ИЛИ ДО ЧЕГО-ТО ОЧЕНЬ БОЛЬШОГО!!!!
        f = (not(x % A == 0)) <= ((x % 12 == 0) <= (not(x % 14 == 0)))
        if f == 0:
            flg = False
    if flg:
        res.append(A)
print(max(res))

####### Тип 3
# https://education.yandex.ru/ege/inf/task/e4ee1ff0-c06e-478d-b397-be872b454f46?clckid=a53c751d
res = []
for A in range(300):
    flg = True
    for x in range(300):
        f = ((x&91) == 0) or (((x&77) == 0) <= ((x&A)!=0))
        if f == 0:
            flg = False
    if flg:
        res.append(A)
print(min(res))