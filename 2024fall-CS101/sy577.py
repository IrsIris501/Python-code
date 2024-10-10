s=list(input())
ansl=[1]
ans=1
for i in range(1, len(s)):
    if s[i]!=s[i-1]:
        ans+=1
    else:
        ansl.append(ans)
        ans=1
print(max(ansl))
