N = int(input())
A = list(map(int,input().split()))
even_list = []
odd_list = []

if len(A)  == 2:
  if A[0] % 2 + A[1] % 2 == 1:
    print(-1)
    exit()

for i in range(N):
  if A[i] % 2 == 0:
    even_list.append(A[i])
    if len(even_list) == 3:
      even_list.sort()
      even_list.pop(0)
  else:
    odd_list.append(A[i])
    if len(odd_list) == 3:
      odd_list.sort()
      odd_list.pop(0)

if len(even_list) == 1:
  print(sum(odd_list))
elif len(odd_list) == 1:
  print(sum(even_list))
else:
  print(max(sum(even_list),sum(odd_list)))