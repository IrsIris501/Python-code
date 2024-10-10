n, w=input().split()
n=int(n)
w=int(w)
a=[]
for i in range(n):
    v, w1=input().split()
    v=int(v)
    w1=int(w1)
    vpw=v/w1
    a.append((w1, vpw))
asort=sorted(a, key=lambda d: d[1], reverse=True)
i=0
value=0
while i<len(asort):
    if w-asort[i][0]>0:
        w-=asort[i][0]
        value+=asort[i][0]*asort[i][1]
        i+=1
    else:
        value+=w*asort[i][1]
        w=0
        break
print(value)

        
    
