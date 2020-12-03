a = open('warandpeace')
a = a.readlines()
itog = []
shetchik = 0
cifra = 1072
while cifra < 1104:
    for shetchik_ciferok in a:
        for q in shetchik_ciferok:
            if q == chr(cifra):
                shetchik += 1
    itog.append([shetchik, chr(cifra)])
    cifra += 1

print(*itog)


