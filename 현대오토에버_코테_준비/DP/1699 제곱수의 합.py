N=int(input())
dp=[0]


for i in range(1,int(N**(0.5))+1):
    for j in range(i**2,(i+1)**2):
        if j==i**2:
            dp.append(1)
        else:
            x=[]
            for k in range(i):
                x.append(dp[j-(i-k)**2]+1)
            dp.append(min(x))
print(dp[N])
