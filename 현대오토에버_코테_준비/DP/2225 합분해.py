N,K=list(map(int,input().split()))
dp=[[0]*(N) for _ in range(K+1)]


print(dp)
for j in range(2,K+1):
    sum=0
    for i in range(N+1):
        sum=sum+dp[j-1][i]
    dp[j-1][i-1]=sum

print(dp[K-1][N-1])