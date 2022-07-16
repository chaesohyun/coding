# N개의 원소 자연수 집합이 주어지면 두 개의 부분집합으로 나누었을 때,
# 두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 YES 출력 아니면 NO출력
import sys
def DFS(v,ssum):
    if v==N:
        if (total-ssum)==ssum:
            print("YES")
            sys.exit(0)
    else:
        DFS(v+1,ssum)
        DFS(v+1,ssum+arr[v])
N=int(input())
arr=list(map(int, input().split()))
total=sum(arr)
DFS(0,0)