import calendar
month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthl=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date=list(map(int, input().split('-')))
n=int(input())
while n>0:
    n-=1
    date[2]+=1
    if calendar.isleap(date[0])==False:
        if date[2]>month[date[1]-1]:
            date[2]=1
            date[1]+=1
            if date[1]>12:
                date[0]+=1
                date[1]=1
    else:
        if date[2]>monthl[date[1]-1]:
            date[2]=1
            date[1]+=1
            if date[1]>12:
                date[0]+=1
                date[1]=1
print('%04d-%02d-%02d'%(date[0], date[1], date[2]))
