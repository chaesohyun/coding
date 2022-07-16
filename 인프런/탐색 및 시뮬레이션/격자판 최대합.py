# N*N 의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의합 중 가장 큰 합을 출력
N=int(input())
x=[]
tmp=[]
for i in range(N):
    a=list(map(int,input().split()))
    x.append(a)
    # 각 행의 합
    tmp.append(sum(a))

# 각 열의 합
for j in range(N):
    hap=0
    for k in range(N):
        hap=hap+x[k][j]
    tmp.append(hap)

# 대각선의 합

ttmp=0
atmp=0
for i in range(N):
    ttmp=ttmp+x[i][i]
    atmp=x[i][N-1-i]
    tmp.append(ttmp)
    tmp.append(atmp)
print(tmp)
print(max(tmp))
