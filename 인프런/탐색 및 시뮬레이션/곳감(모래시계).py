# N*N 격자판에서 회전명령 정보가 2 0 3 이면 2행을 왼쪽으로 3만큼 회전
# 행번호, 방향(왼쪽 0, 오른쪽 1), 회전하는 격자의 수
# M개의 회전명령을 실행하고 모래시계 모양 영역에 감의 총 갯수 출력

N=int(input())
x=[]
for i in range(N):
    arr=list(map(int, input().split()))
    x.append(arr)

M=int(input())
for i in range(M):
    tmp=[]
    for k in range(N):
        tmp.append(0)
    a,b,c=map(int, input().split())
    if b==0:
        for j in range(N):
            tmp[j-c]=x[a-1][j]
        x[a-1]=tmp
    elif b==1:
        for j in range(N):
            tmp[j+c-N]=x[a-1][j]
        x[a-1]=tmp
print(x)
res=0
a=0
b=N-1
for i in range(N):
    if i<N//2:
        for j in range(a,b+1):
            res=res+x[i][j]
        a=a+1
        b=b-1
    else:
        for j in range(a,b+1):
            res=res+x[i][j]
        a=a-1
        b=b+1
print(res)