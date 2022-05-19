# coding: utf-8
# Your code here!
n,W = map(int, input().split(" "))

weight = [0 for i in range(W)]
value = [0 for i in range(n)]
dp = [[] for i in range(n + 1)]

for i in range(n):
    weight[i],value[i] = map(int, input().split(" "))

# dp配列の初期化
for i in range(len(dp)):
    dp[i] = [0 for i in range(W+1)]

for i in range(n):
    for w in range(W+1):
        if(w >= weight[i]):
            dp[i+1][w] = max(dp[i][w-weight[i]] + value[i], dp[i][w])
        else:
            dp[i+1][w] = dp[i][w]

print(dp[n][w])

# for i in dp:
#     print(i)