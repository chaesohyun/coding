# 연산 3가지
# X가 3으로 나눠지면 3으로 나누기
# X가 2로 나눠지면 2로 나누기
# 1 빼기

N=int(input())

# 연산 3개를 사용하여 1을 만들고자 할 때, 연산 횟수의 최솟값 출력
# 메모이제이션
dp=[0]*(N+1)
dp[1]=0
# dfs
for i in range(2,N+1):
    if i%3==0:
        a=dp[i//3]+1
    else: a=1000000

    if i%2==0:
        b=dp[i//2]+1
    else: b=1000000

    c=dp[i-1]+1
    dp[i]=min(a,b,c)
print(dp[N])