def min_diff(arr):
    total = sum(arr)
    ans = float('inf')
    n = len(arr)

    def dfs(i, curr):
        nonlocal ans
        if i == n:
            ans = min(ans, abs(total - 2 * curr))
            return
        dfs(i + 1, curr + arr[i])
        dfs(i + 1, curr)           

    dfs(0, 0)
    print(ans)

n=int(input())
arr=list(map(int,input().split())) 
min_diff(arr)