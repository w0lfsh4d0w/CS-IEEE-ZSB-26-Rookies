def decider(n):
    print(n, end=" ")
    if n == 1:
        return
    if n % 2 == 0:
        decider(n // 2)
    else:
        decider(n * 3 + 1)

n = int(input())
decider(n)
