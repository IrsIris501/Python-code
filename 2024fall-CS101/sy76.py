nums=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
n, k=input().split()
n=int(n)
k=int(k)
s=''
while n>=k:
    i=n%k
    s+=nums[i]
    n=n//k
s+=nums[n]
print(s[::-1])
    
