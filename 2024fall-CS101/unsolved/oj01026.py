while True:
    n=int(input())
    if n==0:
        break
    a=list(map(int, input().split()))
    while True:
        s=input()
        if s=='0':
            break
        for i in range(len(s)):
            if s[i]==' ':
                k=int(s[0:i:])
                s=s[i+1::]
                break
        ls=list(s)
        ls+=[' ']*(n-len(s))
        for i in range(k):
            temp=[' ' for _ in range(n)]
            for j in range(n):
                temp[a[j]-1]=ls[j]
            ls=temp
        print(*ls, sep='')
    
