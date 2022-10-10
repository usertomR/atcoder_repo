# 問題 : https://atcoder.jp/contests/abc070/tasks/abc070_b

A,B,C,D = map(int,input().split())

if C <= A:
  if D <= A:
    print(0)
  elif A < D <= B:
    print(D - A)
  elif B < D:
    print(B - A)
elif A < C <= B:
  if D <= B:
    print(D - C)
  elif B < D:
    print(B - C)
elif B < C:
  print(0)