x=int(input())
while x!=1:
    if x%2!=0:
        print(str(x)+'*3+1='+str(x*3+1))
        x=x*3+1
    else:
        print(str(x)+'/2='+str(x//2))
        x=x//2
        
