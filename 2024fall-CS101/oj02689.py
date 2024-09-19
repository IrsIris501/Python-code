s=list(input())
ans=''
for i in range(len(s)):
    if 65<=ord(s[i])<=90:
        s[i]=chr(ord(s[i])+32)
    elif 97<=ord(s[i])<=122:
        s[i]=chr(ord(s[i])-32)
for i in s:
    ans+=i
print(ans)
