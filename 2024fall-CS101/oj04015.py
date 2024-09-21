try:
    while True:
        s=input()
        flag=1
        if s[0]=='@' or s[0]=='.' or s[-1]=='@' or s[-1]=='.':
            flag=0
        elif '@' not in s:
            flag=0
        else:
            l=list(s)
            l.remove('@')
            if '@' in l:
                flag=0
            else:
                k=list(s)
                n=k.index('@')
                s1=s[n+1:len(s)]
                if '.' not in s1 or s1[0]=='.' or s[n-1]=='.':
                    flag=0
        if flag==0:
            print('NO')
        else:
            print("YES")
except:
    pass
