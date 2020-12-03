a = open('warandpeace')
a = a.readlines()
t = []
b = 0
q = 0
k = 1072
while k < 1103:
    for i in a:
        for d in i:
            if d == chr(k):
                b += 1
        t.append([t, chr(k)])
        k += 1

print(*t)

