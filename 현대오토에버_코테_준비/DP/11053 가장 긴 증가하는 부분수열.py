N=int(input())
A=list(map(int, input().split()))

# 부분 수열의 최대 길이 저장 dp[i] => A[i]가 제일 마지막항일 때, A의 0~(i-1)항 원소 순서는 유지하며 부분 수열 만들 수 있는 최대 길이 의미
dp=[0]*(N+1)
A.insert(0,0)
dp[1]=1

for i in range(2,N+1):
    x=0
    for j in range(i):
        if A[i]>A[j] and dp[j]>x:
            x=dp[j]
    dp[i]=x+1
print(max(dp))
