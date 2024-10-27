h=int(input())
n=int(input())
h=2*h-0.5*n
courses=[]
for i in range(n):
    s, c=input().split()
    s=float(s)
    c=float(c)
    courses.append((s, c))
courses.sort(key=lambda x:x[0]*x[1], reverse=True)
ans=0
for i in range(n):
    if h-5/courses[i][0]>=0:
        ans+=5*courses[i][1]
        h-=5/courses[i][0]
    else:
        ans+=(h*courses[i][0])*courses[i][1]
        break
print('%.1f' % ans)
        
