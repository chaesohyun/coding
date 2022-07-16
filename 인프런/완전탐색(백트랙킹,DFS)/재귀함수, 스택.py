N=int(input())
def DFS(x):
    if x>0:
        print(x, end=' ')
        DFS(x-1)

DFS(N)