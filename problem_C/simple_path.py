# https://atcoder.jp/contests/abc270/tasks/abc270_c
# めっちゃ苦戦した...C問題から、処理スピードを意識したコーディングをする！

import sys
sys.setrecursionlimit(10**7) # 再帰回数の設定


N,X,Y = map(int,input().split())

# 2点のノードのつながりのリスト。
two_nodes_connection_list = [[] for _ in range(N+1)]
two_nodes_connection_list[0] = ["#"]
# 回答
answer_list =[]

for i in range(N-1):
  u,v = map(int,input().split())
  two_nodes_connection_list[u].append(v)
  two_nodes_connection_list[v].append(u)


def dfs(start):
  answer_list.append(start)

  if  start == Y:
    print(*answer_list)
    exit()
  
  for next_node in two_nodes_connection_list[start]:
    # answer_listは、始点から現在のノードまでの辿り方を記録。
    #つまり来た道を戻ることになるかどうかの判定。
    if next_node != answer_list[len(answer_list) - 2]:
      dfs(next_node)
  
  answer_list.pop()

dfs(X)