# 問題 : https://atcoder.jp/contests/abc096/tasks/abc096_c

H,W = map(int,input().split())
S_i_j = []
for i in range(H):
  read_line = input()
  S_i_j.append(read_line)

# (行の変化量、列の変化量)
valid_move = [(-1,0),(1,0),(0,-1),(0,1)]


for i in range(H):
  for j in range(W):
    if S_i_j[i][j] == "#":
      for di,dj in valid_move:
        if 0 <= i + di < H and 0 <= j + dj < W and S_i_j[i+di][j+dj] == "#":
          break
        # 上下左右に「#」がなかったら、「No」を出力し終了
        if di == 0 and dj == 1:
          print("No")
          exit()

print("Yes")

