N, K=input().split()
N=int(N)
K=int(K)
counter=0
while(N>0):
    N=N//K
    counter+=1

print(counter)
    