nmale=int(input())
male=list(map(int, input().split()))
male.sort()
nfemale=int(input())
female=list(map(int, input().split()))
female.sort()
ans=0
while female!=[] and male!=[]:
    if abs(female[-1]-male[-1])<=1:
        female.pop(-1)
        male.pop(-1)
        ans+=1
    else:
        if female[-1]<male[-1]-1:
            male.pop(-1)
        elif female[-1]>male[-1]+1:
            female.pop(-1)
print(ans)
