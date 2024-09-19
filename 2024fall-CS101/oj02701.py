ans=0
n=int(input())
for i in range(1, n+1):
    if '7' not in str(i) and i%7!=0:
        ans+=i**2
print(ans)
