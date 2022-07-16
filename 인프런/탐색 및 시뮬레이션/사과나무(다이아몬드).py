# N*N 격자판 N은 항상 홀수
# 사과를 수확할 때, 다이아몬드 모양의 격자판만 수확하고 나머지는 남겨놓는다.
# 수확하는 사과의 총 갯수 출력

N=int(input())
x=[]
for i in range(N):
    a=list(map(int, input().split()))
    x.append(a)

tmp=0
a=N//2
b=N//2
for i in range(N):
    if i<N//2:
        for j in range(a,b+1):
            tmp=tmp+x[i][j]
        a=a-1
        b=b+1
    else:
        for j in range(a, b+1):
            tmp=tmp+x[i][j]
        a=a+1
        b=b-1

print(tmp)