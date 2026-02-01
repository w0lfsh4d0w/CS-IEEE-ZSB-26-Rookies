import math

X = int(input())

best_a = 1
best_b = X
best_max = X 

for a in range(1, int(math.isqrt(X)) + 1):
    if X % a == 0:
        b = X // a
        
        if a * b // math.gcd(a, b) == X:
            if max(a, b) < best_max:
                best_max = max(a, b)
                best_a = a
                best_b = b

print(best_a, best_b)
