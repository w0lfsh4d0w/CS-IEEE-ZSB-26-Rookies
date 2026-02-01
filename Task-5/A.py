MAX = 10**6 + 1
div_count = [0] * MAX

for i in range(1, MAX):
    for j in range(i, MAX, i):
        div_count[j] += 1

n = int(input())
for _ in range(n):
    x = int(input())
    print(div_count[x])
