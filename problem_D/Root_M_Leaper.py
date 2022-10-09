# 問題 : https://atcoder.jp/contests/abc272/tasks/abc272_d
# dequeueを使おう。: https://note.nkmk.me/python-collections-deque/
# 以下2行に合わせ実装すると、処理速度が倍近くになった。謎。
# if __name__ == "__main__":
#   answer()
from collections import deque
def answer():
  N,M = map(int,input().split())

  square_n_map = [[-1]*N for _ in range(N)]
  square_n_map[0][0] = 0

  way_of_move = []

  for i in range(N):
    for j in range(N):
      if i**2 + j**2 == M:
        way_of_move.append((i,j))
        way_of_move.append((i,-j))
        way_of_move.append((-i,j))
        way_of_move.append((-i,-j))

  queue = deque()
  queue.append((0,0))

  while queue:
    location_x,location_y = queue.popleft()

    for move in way_of_move:
      dx,dy = move
      if 0 <= location_x + dx < N and 0 <= location_y + dy < N:
        if square_n_map[location_y + dy][location_x + dx] > square_n_map[location_y][location_x] + 1:
          square_n_map[location_y + dy][location_x + dx] = square_n_map[location_y][location_x] + 1
          queue.append((location_y + dy,location_x + dx))
          continue
        elif square_n_map[location_y + dy][location_x + dx] == -1:
          square_n_map[location_y + dy][location_x + dx] = square_n_map[location_y][location_x] + 1
          queue.append((location_y + dy,location_x + dx))

  for i in range(N):
      print(" ".join(map(str,square_n_map[i])))

if __name__ == "__main__":
  answer()