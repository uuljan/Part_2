age = list(range(0,27+1))
print(age)
end = age[-1]

if end % 2 != 0:
    for i in age:
        if i % 2 != 0:
            print(i)
else:
    for j in age:
        if(j % 2 == 0):
            print(j)
