def countOddNumbers(numbers): 
    sum = 0
    for num in numbers:
        if num%2!=0:
            sum += numbers.count(num)
    return sum 

def countEverNumbers(numbers): 
    sum2 = 0
    for num2 in numbers:
        if num2 % 2 == 0:
            sum2 += numbers.count(num2)
    return sum2 

print(countOddNumbers(range(1, 10)))
print(countEverNumbers(range(1, 10)))