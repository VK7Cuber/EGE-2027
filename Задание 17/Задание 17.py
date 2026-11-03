# ШАБЛОН
# ---------------------------------------------------------
# 1. Читаем файл
# f = open("17.txt")
# s = [int(i) for i in f]
#
# # 2. Поиск вспомогательной переменной
# r = []
# for i in range(len(s)):
#     if ...s[i]...: # какое-то условие
#         r.append(s[i])
# m = min(r) # или, допустим, max(r)

# 3. Сама задача
# res = []
# for i in range(len(s) - (k-1)): # где k - количество рассматриваемых элементов. Например, если рассматриваем тройки, k = 3
#     if ...s[i]...s[i+1]...s[i+2]...:
#         res.append(s[i] + s[i+1] + s[i+2])
#
# print(len(res), min(res))




# Пример 1
# ---------------------------------------------------------
# s = [int(i) for i in open("17.txt")]
# m = max(filter(lambda x: str(x)[-1] == "3" and len(str(abs(x))) == 4, s))
# r = []
# for i in range(len(s) - 2):
#     e1, e2, e3 = s[i], s[i+1], s[i+2]
#     if int(str(e1)[-1] == "3" and len(str(abs(e1))) == 4) \
#         + int(str(e2)[-1] == "3" and len(str(abs(e2))) == 4) \
#         + int(str(e3)[-1] == "3" and len(str(abs(e3))) == 4) == 2:
#         if (e1 + e2 + e3) > m:
#             r.append(e1 + e2 + e3)
# print(len(r), max(r))




# Пример 2
# ---------------------------------------------------------
# # Читаем файл
# s = [int(i) for i in open("17-3.txt", "r")]
#
# # Поиск вспомогательной переменной
# m = max(filter(lambda x: str(x)[-2:] == "17", s))
#
# # Решение задачи
# r = []
# for i in range(len(s) - 2):
#     e1, e2, e3 = s[i], s[i+1], s[i+2]
#     if (int(100 <= abs(e1) <= 999) + int(100 <= abs(e2) <= 999) + int(100 <= abs(e3) <= 999)) == 1:
#         if (e1 + e2 + e3) < m:
#             r.append(e1+e2+e3)