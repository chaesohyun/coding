# 여러 단위의 동전이 있을 때, 거스름돈을 가장 적은 수의 동전으로 교환
import sys
def DFS(index,sum):
    global res
    if sum>M:
        return
    if sum==M:
        if index<res:
            res=index
    else:
        for i in range(N):
            DFS(index+1,sum+a[i])

N=int(input()) # 동전 종류의 갯수
a=list(map(int, input().split())) # 동전 종류
M=int(input()) # 거슬러 줄 금액
res=2147000000
a.sort(reverse=True)
DFS(0,0)
print(res)
