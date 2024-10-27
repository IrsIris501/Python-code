n=int(input())
print(n)
tmonths=['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk', 'ok', 'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']
hmonths=['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax', 'zac', 'ceh', 'mac', 'kankin', 'muan', 'pax', 'koyab', 'cumhu', 'uayet']
for i in range(n):
    dateh=input().split()
    dayh=int(dateh[0][:-1])
    monthh=hmonths.index(dateh[1])
    yearh=int(dateh[2])
    day=365*yearh+20*monthh+dayh
    namet=tmonths[day%20]
    numbert=day%13+1
    yeart=day//260
    print(numbert, namet, yeart)
    
    
    
