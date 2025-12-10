t=int(input())
for _ in range(t):
  n=int(input())
  array=list(map(int, input().split()))
  common=0
  if array[0]==array[1] or array[0]==array[2]:
    common=array[0]
  else:
    common=array[1]
  for i in range(n):
    if array[i] !=common:
      print(i+1)
      break
    
  
