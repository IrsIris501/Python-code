s=int(input())
s=bin(s)
s=s[2::]
s1=s[::-1]
if s1==s:
    print("Yes")
else:
    print("No")
