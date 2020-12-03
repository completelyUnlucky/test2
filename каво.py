import random
a = []
z = []
m = 0
n = 0
for i in range(6):
    a.append(random.randint(0, 101))

while m != 6:
    k = min(a)
    a.remove(k)
    z.append(k)
    m = m + 1

print(z)
