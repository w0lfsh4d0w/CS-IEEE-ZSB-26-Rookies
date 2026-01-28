s = input().strip()
s = sorted(s)      
n = len(s)

used = [False] * n
result = []

def backtrack(current):
    if len(current) == n:
        result.append(''.join(current))
        return

    for i in range(n):
   
        if used[i]:
            continue

    
        if i > 0 and s[i] == s[i-1] and not used[i-1]:
            continue

        used[i] = True
        current.append(s[i])

        backtrack(current)

        current.pop()
        used[i] = False


backtrack([])

print(len(result))
for r in result:
    print(r)
