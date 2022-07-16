# 바둑이들을 데리고 시장에 가려고 한다.
# 트럭은 C킬로그램 넘게 태울 수 없다.
# 바둑이 N마리, 각 바둑이의 무게가 W일 때, 트럭에 태울 수 있는 가장 무거운 무게구하는 프로그램
import sys



def DFS(v,sum):
    global result
    if sum>C:
        return
    if v==N:
        if sum>result:
            result=sum
    else:
        DFS(v+1,sum)
        DFS(v+1,sum+arr[v])

C,N=map(int, input().split())
arr=[]
for i in range(N):
    arr.append(int(input()))
result=-22222222222222
DFS(0,0)

print(result)