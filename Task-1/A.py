n = int(input())
problemSolved = 0
while n:
    a, b, c = map(int, input().split())
    s = a + b + c

    if s >= 2:
        problemSolved += 1

    n -= 1

print(problemSolved)
