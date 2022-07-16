N=int(input())
s=list(map(int, input().split()))
s.insert(0,0)

dp=[0]

for i in range(1,N+1):
    tmp=[]
    tmp.append(s[i])
    for j in range(1,i):
        tmp.append(s[j]+dp[i-j])
    dp.append(min(tmp))

print(dp[N])