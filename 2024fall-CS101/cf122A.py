n=int(input())
s=set(str(n))
if s=={4, 7} or s=={4} or s=={7}:
    print("YES")
elif n%4==0 or n%7==0 or n%47==0 or n%74==0 or n%447==0 or n%474==0 or n%477==0 or n%747==0 or n%774==0:
    print("YES")
else:
    print("NO")
