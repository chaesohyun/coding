# 자연수 N이 주어지면 1~N까지 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램
# 상태트리를 먼저 그릴 것
# 1을 포함하느냐 안하느냐, 2를 ...
# D(1)=D(2),D(2) ==D(3)D(3)D(3)D(3)...
# check 라는 리스트를 만들어서 1,2,3 을 포함하느냐 안하느냐를 0,1을 넣어 구분

def DFS(k):
    if k==N+1: # 말단 노드에서 부분집합 출력
        for i in range(1,N+1):
            if check[i]==1:
                print(i,end='')
        print()
    else:
        check[k]=1
        DFS(k+1)
        check[k]=0
        DFS(k+1)


N=int(input())
check=[0]*(N+1)
DFS(1)