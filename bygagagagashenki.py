a = 'I love Sergey'
# a = a.readlines()
k = 0
lines = ['']
for i in a:
    if i != ' ':
        lines[k] += i
    else:
        lines.append('')
        k += 1

for i in lines:
    print(i)
# print(a)
