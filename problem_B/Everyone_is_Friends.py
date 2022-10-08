N,M = map(int,input().split())
k_x = []

for i in range(M):
  read_line = list(map(int,input().split()))
  read_line.pop(0)
  k_x.append(read_line)

for person_1 in range(1,N+1):
  for person_2 in range(person_1+1,N+1):
    for m in range(M):
      if person_1 in k_x[m] and person_2 in k_x[m]:
        break
      if m == M - 1:
        print("No")
        exit()

print("Yes")