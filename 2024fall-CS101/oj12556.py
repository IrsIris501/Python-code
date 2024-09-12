s=input()
s=s.lower()
c=0
for i in range(len(s)):
    try:
        if s[i]==s[i+1]:
            c+=1
        else:
            print('('+s[i]+','+str(c+1)+')', end='')
            c=0
    except:
        print('('+s[i]+','+str(c+1)+')', end='')
