plus = []
minus = []
def numbers():
    for num in range(-10 , 10):
        if num < 0:
            plus.append(num)
        elif num > 0:
            minus.append(num)
    print(plus)
    print(minus)

numbers()