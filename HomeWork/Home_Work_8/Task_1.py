"""
Задание 1.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9
Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix():
    def __init__(self, arr):
        self.arr = arr

    def __str__(self):
        return '\n'.join(str(s) for s in self.arr)

    def __add__(self, other):
        return Matrix([[j[0] + j[1] for j in zip(i[0], i[1])] for i in zip(self.arr, other.arr)])


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print('matrix1:', matrix1, end='\n\n', sep='\n')
print('matrix2:', matrix2, end='\n\n', sep='\n')
print('matrix1 + matrix2:', matrix1 + matrix2, end='\n\n', sep='\n')

