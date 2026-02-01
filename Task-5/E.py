t=int(input())
while t:
    number=int(input())
    if number%2 !=0:
        print(0)
    else:
        print((number // 4) + 1)
    t-=1
    
