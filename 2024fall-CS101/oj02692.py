def test(coin, temp):
    for i in range(len(temp)):
        a=0
        b=0
        for j in range(4):
            a+=coin[ord(temp[i][0][j])-65]
            b+=coin[ord(temp[i][1][j])-65]
        if b-a<=0:
            return 0
    return 1
n=int(input())

for i in range(n):
    coin=[1]*12
    w=0
    temp=[]
    for _ in range(3):
        a, b, s=input().split()
        if s=="even":
            for j in range(4):
                coin[ord(a[j])-65]=0
                coin[ord(b[j])-65]=0
        else:
            if s=='up':
                temp.append([b, a])
            if s=="down":
                temp.append([a, b])
    for i in range(12):
        if coin[i]:
            tc=[0]*12
            tc[i]=1
            if test(tc, temp):
                print(chr(i+65)+" is the counterfeit coin and it is heavy.")
                break
            tc[i]=-1
            if test(tc, temp):
                print(chr(i+65)+" is the counterfeit coin and it is light.")
                break
                
            
    
