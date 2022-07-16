# 2Xn 직사각형을 1x2, 2x1타일로 채우는 방법의 수
n=int(input())
# 메모이제이션
dp=[0,1,2]

for i in range(3,n+1):
    dp.append(dp[i-1]+dp[i-2])

print(dp[n]%10007)