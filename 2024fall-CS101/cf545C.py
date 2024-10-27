n=int(input())
trees=[]
for i in range(n):
    x, h=map(int, input().split())
    trees.append([x, h])
ans=0
flag=[]
for i in range(n):
    if i!=0:
        if trees[i][0]-trees[i][1]>max(trees[i-1][0]+trees[i-1][1]*flag[i-1], trees[i-1][0]):
            ans+=1
            flag.append(-1)
        else:
            if i!=n-1:
                if trees[i][0]+trees[i][1]<trees[i+1][0]:
                    ans+=1
                    flag.append(1)
                else:
                    flag.append(0)
            else:
                ans+=1
                flag.append(1)
    else:
        flag.append(-1)
        ans+=1
print(ans)
