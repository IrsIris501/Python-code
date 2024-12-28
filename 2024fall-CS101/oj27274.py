import math
s=input()
m=math.floor(math.log2(len(s)))
ans=''
if m%2==0:
    for i in range(m//2):
        ans+=s[2**i-1]
        ans+=s[2**(m-i)-1]
    ans+=s[2**(m//2)-1]
else:
    for i in range(m//2+1):
        ans+=s[2**i-1]
        ans+=s[2**(m-i)-1]
print(ans)
