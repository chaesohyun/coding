# N*N 격자판에는 지역의 높이가 쓰여있음
# 각 격자판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역이다.
# 봉우리 지역이 몇 개 있는지 알아내는 프로그램
# 격자의 가장자리는 0으로 초기화

N=int(input())
x=[]
test=[]
for i in range(N+2):
    test.append(0)

for i in range(N):
    arr=list(map(int, input().split()))
    arr.insert(0,0)
    arr.insert(N+1,0)
    x.append(arr)

x.insert(0,test)
x.insert(N+1,test)

count=0
for i in range(1,N+1):
    for j in range(1,N+1):
        tmp=[]
        tmp.append(x[i][j])
        tmp.append(x[i-1][j])
        tmp.append(x[i+1][j])
        tmp.append(x[i][j-1])
        tmp.append(x[i][j+1])
        if max(tmp)==x[i][j]:
            count=count+1
print(count)
