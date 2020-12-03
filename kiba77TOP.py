import random
massiv1 = [10, 44, 3, 1, 13, 66, 19]
def my_min(massiv1):
    massiv2 = []
    sravnenie = massiv1[0]
    for i in range(len(massiv1)):
        for i in range(len(massiv1)):
            if sravnenie > massiv1[i]:
                 sravnenie = massiv1[i]
    massiv2.append(massiv1.pop(massiv1.index(sravnenie)))
    return massiv2
print(my_min(massiv1))
print(massiv1)
