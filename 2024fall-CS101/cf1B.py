n=int(input())
nums=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(n):
    s=input()
    flag=0
    for i in range(len(s)-1):
        if s[i] in nums and s[i+1] not in nums:
            flag=i
            break
    if flag:
        r=int(s[1:i+1])
        c=int(s[i+2::])-1
        ans=chr(c%26+65)
        c=c//26
        while c>0:
            c-=1
            a=c%26
            c=c//26
            ans+=chr(a+65)
        
        print(ans[::-1]+str(r))
    else:
        for i in range(len(s)-1):
            if s[i] not in nums and s[i+1] in nums:
                flag=i+1
                break
        c=s[:flag:]
        r=s[flag::]
        ans=0
        for i in c:
            ans*=26
            ans+=ord(i)-64
        print("R"+r+"C"+str(ans))
        
    
    
