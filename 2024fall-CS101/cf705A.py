n=int(input())
s=''
for i in range(n):
    if i!=0:
        if i%2==0:
            s+='that I hate '
        else:
            s+='that I love '
    else:
        s+='I hate '
s+='it'
print(s)
