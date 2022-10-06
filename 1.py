ARRAY = []
min_lmnt = 10 ** 100
count = 0
n = int(input('Введите количество элементов в списке: '))
for i in range(n):
    ARRAY.append(int(input('Введите элемент, нажмите Enter: ')))
DELTA = int(input('Введите значение дельты: '))
for lmnt in range(len(ARRAY)):
    if ARRAY[lmnt] < min_lmnt:
        min_lmnt = ARRAY[lmnt]
for lmnt_1 in range(len(ARRAY)):
    if ARRAY[lmnt_1] - DELTA == min_lmnt:
        count += 1
print('В массиве', count, 'элементов, отличающихся от минимального на', DELTA)
