t = int(input())

for _ in range(t):
    n = int(input())
    found = False

    for a in range(2, int(n**0.5) + 1):
        if n % a == 0:
            n1 = n // a
            for b in range(a + 1, int(n1**0.5) + 1):
                if n1 % b == 0:
                    c = n1 // b
                    if c != a and c != b and c >= 2:
                        print("YES")
                        print(a, b, c)
                        found = True
                        break
            if found:
                break

    if not found:
        print("NO")
