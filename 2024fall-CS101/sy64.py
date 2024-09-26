n=int(input())
l=list(map(int, input().split()))
k=int(input())
a=[]
for i in range(n):
    a.append(i)
    
ans=0
for i in a:
    for j in range(i+1, len(l)):
        if l[i]+l[j]==k:
            ans+=1

            break
            
        
    
print(ans)
