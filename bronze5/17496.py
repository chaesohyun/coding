N,T,C,P=map(int,input().split())
count=0
for i in range(1,int(N/T)+1):
    if 1+i*T<=N:
        count=count+1

print(count*C*P)


