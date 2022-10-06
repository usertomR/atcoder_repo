# 問題 : https://atcoder.jp/contests/abs/tasks/arc065_a
# 解説 : https://qiita.com/drken/items/fd4e5e3630d0f5859067#%E7%AC%AC-9-%E5%95%8F--abc-049-c---daydream-300-%E7%82%B9

S = input()

divide = ["dream","dreamer","erase","eraser"]

# 後ろから解くかわりにすべての文字列を「左右反転」する
S = S[::-1]
for i in range(len(divide)):
  divide[i] = divide[i][::-1]

# どこの文字から単語を見つけるかを示すポインタ。Sの添字の値
i = 0

while i != len(S):
  #  divideの文字で区切れるかどうかのフラグ
  divide_flag = False
  for j in range(len(divide)):
    string = divide[j]
    if S[i:i+len(string)] == string:
      i = i + len(string)
      divide_flag = True
      break
  
  if divide_flag == False:
    print("NO")
    exit()

print("YES")

