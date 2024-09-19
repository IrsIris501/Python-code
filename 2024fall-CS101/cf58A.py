s=input()
a=['h', 'e', 'l', 'l', 'o']
for i in s:
    if a!=[] and i==a[0]:
        a.pop(0)
if a==[]:
    print('YES')
else:
    print('NO')
