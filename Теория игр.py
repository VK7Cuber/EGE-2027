# Теория игр
# В примерах считаем, что Петя проигрывает, Ваня выигрывает

# Для одной кучи:
# ---------------------------------------------------------------------------------------------------------
# Вариант 1
# def f(stones, moves) -> bool:
#     if stones >= 124: return moves % 2 == 0
#     if moves == 0: return False
#     new_moves = [
#         f(stones+1, moves-1),
#         f(stones+5, moves-1),
#         f(stones*3, moves-1)
#     ]
#     return any(new_moves) if moves % 2 == 1 else all(new_moves)
#
# print("Задача 19:", [s for s in range(1, 124) if f(s, 2)])
# print("Задача 20:", [s for s in range(1, 124) if f(s, 3) and not f(s, 1)])
# print("Задача 21:", [s for s in range(1, 124) if f(s, 4) and not f(s, 2)])
#
#
# # Вариант 2
# from functools import lru_cache
# def get_moves_list(stones): # получение списка всех возможных продолжений игры (список возможных ходов)
#     first = stones
#     # first, second = stones # если у нас 2 кучи
#     return (first + 1), (first + 5), (first * 3)
#
# @lru_cache(None)
# def f(stones):
#     if stones >= 124: # условия победы
#         return "WIN"
#     if any(f(x) == "WIN" for x in get_moves_list(stones)): # если есть хотя бы один ход, который даёт победу
#         return "П1" # победа Пети первым ходом
#     if all(f(x) == "П1" for x in get_moves_list(stones)):  # если любой из возможных ходов даёт победу Пети первым ходом
#         return "В1" # победа Вани первым ходом
#     if any(f(x) == "В1" for x in get_moves_list(stones)): # если каким-то из ходов может выиграть Ваня
#         return "П2" # победа Пети вторым ходом
#     if all(f(x) in ("П1", "П2") for x in get_moves_list(stones)):  # если любой из ходов позволяет Пете выиграть либо первым, либо вторым ходом
#         return "В2" # победа Вани вторым ходом



# Для двух куч:
# ---------------------------------------------------------------------------------------------------------
# Вариант 1
def f(stones_1, stones_2, moves) -> bool:
    if stones_1 + stones_2 >= 133: return moves % 2 == 0
    if moves == 0: return False
    new_moves = [
        f(stones+1, moves-1),
        f(stones+5, moves-1),
        f(stones*3, moves-1)
    ]
    return any(new_moves) if moves % 2 == 1 else all(new_moves)

print("Задача 19:", [s for s in range(1, 124) if f(s, 2)])
print("Задача 20:", [s for s in range(1, 124) if f(s, 3) and not f(s, 1)])
print("Задача 21:", [s for s in range(1, 124) if f(s, 4) and not f(s, 2)])


# Вариант 2
from functools import lru_cache
def get_moves_list(stones): # получение списка всех возможных продолжений игры (список возможных ходов)
    first = stones
    # first, second = stones # если у нас 2 кучи
    return (first + 1), (first + 5), (first * 3)

@lru_cache(None)
def f(stones):
    if stones >= 124: # условия победы
        return "WIN"
    if any(f(x) == "WIN" for x in get_moves_list(stones)): # если есть хотя бы один ход, который даёт победу
        return "П1" # победа Пети первым ходом
    if all(f(x) == "П1" for x in get_moves_list(stones)):  # если любой из возможных ходов даёт победу Пети первым ходом
        return "В1" # победа Вани первым ходом
    if any(f(x) == "В1" for x in get_moves_list(stones)): # если каким-то из ходов может выиграть Ваня
        return "П2" # победа Пети вторым ходом
    if all(f(x) in ("П1", "П2") for x in get_moves_list(stones)):  # если любой из ходов позволяет Пете выиграть либо первым, либо вторым ходом
        return "В2" # победа Вани вторым ходом
