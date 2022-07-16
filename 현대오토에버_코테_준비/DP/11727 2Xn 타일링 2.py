# 2Xn 직사각형을 1X2, 2X1, 2X2로 채우는 방법의 수
n=int(input())

# 메모이제이션
dp=[0,1,3]
for i in range(3,n+1):
    dp.append(dp[i-1]+2*dp[i-2])

print(dp[n]%10007)