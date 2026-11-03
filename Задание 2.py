"""
Варианты решения задания на алгебру логики (задание 2)
"""
# Вариант 1:

# print("x y z w")
# for x in 0,1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = not ((((((w and x) == x) or 1) <= z) or (not x)) and y)
#                 if f == 0:
#                     print(x, y, z, w)
#
# # y x z w



# Вариант 2:
# from itertools import product
# print("x y z w")
# for x, y, z, w in product([0, 1], repeat=4):
#     f = not ((((((w and x) == x) or 1) <= z) or (not x)) and y)
#     if f == 0:
#         print(x, y, z, w)