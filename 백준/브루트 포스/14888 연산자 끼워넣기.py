# N개의 수열과 수와 수 사이에 넣을 N-1개의 연산자가 주어진다
# 연산자는 +,-,x,/
# 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램
import sys
N=int(input())
A=list(map(int, input().split())) # 총 N 개
a,b,c,d=map(int, input().split()) # +,-,x,/ 의 갯수 # 총 N-1 개
mx,mn = -sys.maxsize -1, sys.maxsize
print(mx,mn)
def dfs(num,idx,add,sub,mul,div):
    global mx
    global mn
    if idx==N:
        mx=max(mx,num)
        mn=min(mn,num)
        return
    if add>0:
        dfs(num+A[idx],idx+1,add-1,sub,mul,div)
    if sub>0:
        dfs(num-A[idx],idx+1,add,sub-1,mul,div)
    if mul>0:
        dfs(num*A[idx],idx+1,add,sub,mul-1,div)
    if div>0:
        dfs(int(num/A[idx]),idx+1,add,sub,mul,div-1)
dfs(A[0],1,a,b,c,d)
print(mx)
print(mn)