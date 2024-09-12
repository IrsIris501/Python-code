day=["Sunday", "Monday", 'Tuesday', 'Wednesday', 'Thursday', 'Friday', "Saturday"]
n=int(input())
for i in range(n):
    a=input()
    c=int(a[0:2])
    y=int(a[2:4])
    m=int(a[4:6])
    if m<=2:
        m+=12
        if y!=0:
            y-=1
        else:
            y=99
            c-=1
    
    d=int(a[6:8])
    w=(y+int(y/4)+int(c/4)-2*c+int(26*(m+1)/10)+d-1)%7
    print(day[w])
