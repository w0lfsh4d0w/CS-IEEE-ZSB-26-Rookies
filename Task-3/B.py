n, k = map(int, input().split())
r = list(map(int, input().split()))

y = r[:]
cnt = 0

for i in range(1, 2*n, 2):  
    if cnt < k and y[i] - 1 > y[i-1] and y[i] - 1 > y[i+1]:
        y[i] -= 1
        cnt += 1

print(*y)
print("Helllo")
