# 問題 : https://atcoder.jp/contests/abc075/tasks/abc075_b
# なぜかWAになる。

H,W = map(int,input().split())
S_list = []
answer_list = [[] for _ in range(H)]

for _ in range(H):
  S_list.append(input())

# 一点ずつ調べる。調べ終わったら数字に変える
for i in range(H):
  for j in range(W):
    # 爆弾が周りに何個あるかを表す
    sum_bomb = 0
    # 周りの点を調べる。
    for x in [-1,0,1]:
      for y in [-1,0,1]:
        if x == 0 and y == 0:
          continue
        if j + x >= 0 and j + x < W and i + y >= 0 and i + y < H and S_list[i+y][j+x] == "#":
          sum_bomb = sum_bomb + 1
    if S_list[i][j] == "#":
      answer_list[i].append("#")
    else:
      answer_list[i].append(str(sum_bomb))


for i in range(H):
  answer_line = ""
  for j in range(W):
    answer_line = answer_line + answer_list[i][j]
  print(answer_line)
  