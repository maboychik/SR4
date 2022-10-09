A = []
B = []
C = []
n1 = int(input('Введите количество элементов в массиве A: '))
for i1 in range(n1):
    A.append(float(input('Введите элемент массива A, нажмите Enter: ')))

print('-' * 43)
n2 = int(input('Введите количество элементов в массиве B: '))
for i2 in range(n2):
    B.append(float(input('Введите элемент массива B, нажмите Enter: ')))

for lmnt in range(len(A)):
    if A[lmnt] in B:
        C.append(A[lmnt])
print('-' * 43)
print('Для массивов A:', A, 'и B:', B, 'общие элементы составляют массив C:', set(C))
