pig=[]
while True:
    try:
        ins=input()
    except:
        break
    if ins=='pop':
        if pig!=[]:
            pig.pop()
    elif ins=="min":
        if pig!=[]:
            print(pig[-1][1])
    else:
        tmp=ins.split()
        a=int(tmp[1])
        if pig!=[]:
            if a<pig[-1][1]:
                pig.append((a, a))
            else:
                pig.append((a, pig[-1][1]))
        else:
            pig.append((a, a))
