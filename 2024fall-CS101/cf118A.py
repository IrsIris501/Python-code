s=input().lower()
vowels=['a', 'e', 'i', 'o', 'u', 'y']
ans=''
for i in range(len(s)):
    if s[i] not in vowels:
        ans+=('.'+s[i])
print(ans)
