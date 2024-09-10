import random
while True:
    s = ''
    for i in range(5):
        a = random.randint(97,122)
        s += chr(a)
    print(s)
    while True:
        b = input()
        if b == s:
            break
    
    
