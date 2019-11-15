x = int(input("Введите число: "))
print("Все квадраты чисел до введенного числа:")
for i in range(1, x):
    if i**2 <= x:
        print(i**2)
