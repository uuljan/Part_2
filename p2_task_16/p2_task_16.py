earth_weight = 70
print("Мой веc на земле: ", earth_weight)

moon_weight = earth_weight * 0.165
print("Мой вес на луне: ", moon_weight)


for i in range(1, 15+1):
    x = earth_weight + i
    # i+=1
    print("Мой вес на земле через {} :".format(i), x, "---- Мой вес на луне {} через:".format(i), x * 0.165)

    