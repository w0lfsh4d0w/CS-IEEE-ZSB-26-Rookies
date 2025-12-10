n = int(input())
s = input()
new_s = set(s.lower())

if len(new_s) == 26:
    print("YES")
else:
    print("NO")
