while True:
    try:
        a, b=input().split()
        a=list(a)
        b=list(b)
    except:
        break
    dp=[]
    for i in range(len(a)+1):
        dp.append([])
        for j in range(len(b)+1):
            dp[i].append(0)
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]:
                dp[i+1][j+1]=dp[i][j]+1
            else:
                dp[i+1][j+1]=max(dp[i][j+1], dp[i+1][j])
    print(dp[-1][-1])

