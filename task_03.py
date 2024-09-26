# 3. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код,
# решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

def chess_queen(corr_x: list, corr_y: list) -> bool:
    flag = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                flag = False
        if flag:
            return True
        return False


n = 8
x = list()
y = list()
for i in range(n):
    new_x, new_y = [int(i) for i in input().split()]
    x.append(new_x)
    y.append(new_y)

print(chess_queen(x, y))
