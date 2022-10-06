# 問題 : https://atcoder.jp/contests/abc271/tasks/abc271_b
# 解説 : https://atcoder.jp/contests/abc271/editorial/4916

N,Q = map(int,input().split())

L_and_aij = []
# i(1≤i≤N) 番目の数列のiに合わせる。添字0を#にする。
L_and_aij.append(["#"])

query_list = []
# k(1≤k≤Q) 番目のクエリのkに合わせる。添字0を#にする。
query_list.append(["#"])

answer = []

for i in range(1,N+1):
  read_line = list(map(int,input().split()))
  L_and_aij.append(read_line)

for q in range(Q):
  read_line = list(map(int,input().split()))
  query_list.append(read_line)

for k in range(1,Q+1):
  sk_tk = L_and_aij[query_list[k][0]][query_list[k][1]]
  answer.append(sk_tk)

for i in range(Q):
  print(answer[i])