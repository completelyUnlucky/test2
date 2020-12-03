import random
a = [random.randint(10, 99) for i in range(10)]
for i in a:
    print(i)
print()
for i in range(len(a)):
    print(a[i])