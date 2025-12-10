t=int(input())
for i in range(t) :
    n=int(input())
    s=input()
    ballons=0
    solved_proplems=[]
    for ch in s:
        if ch in solved_proplems:
            ballons+=1
        else:
            ballons+=2
            solved_proplems.append(ch)
    print(ballons)
