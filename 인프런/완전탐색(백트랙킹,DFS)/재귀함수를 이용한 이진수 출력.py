# 10 진수가 입력되면 2진수로 변환하는 프로그램

n=int(input()) # 10진수
res=[]

def dfs(x):
    if x==0:
        return
    else:
        dfs(x//2)
        print(x % 2, end='')
dfs(n)