numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
change = []
for elem in numbers:
    if elem > 0:
        change.append(1)
    elif elem < 0:
        change.append(-1)
    else:
        change.append(0)

print(numbers)
print(change)