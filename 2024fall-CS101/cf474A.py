a='qwertyuiop asdfghjkl; zxcvbnm,./'
b=input()
if b=='R':
    c=-1
else:
    c=1
d=input()
ans=''
for i in d:
    j=a.index(i)
    ans+=a[j+c]
print(ans)
