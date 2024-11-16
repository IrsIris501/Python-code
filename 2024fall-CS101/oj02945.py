k=int(input())
mis=list(map(int, input().split()))
ans=[0]*k
ans[0]=1
for i in range(1, k):
    for j in range(i):
        if mis[j]>=mis[i] and ans[j]>ans[i]:
            ans[i]=ans[j]
    ans[i]+=1
print(max(ans))
