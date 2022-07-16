# 1~N 번호가 적힌 구슬
# 중복을 허락하여 뽑아 일렬로 나열하는 방법 모두 출력
def DFS(v):
    global cnt
    if v==M:
        for i in ch:
            print(i,end=' ')
        print()
        cnt = cnt + 1
    else:
        for i in range(1,N+1):
            ch[v]=i
            DFS(v+1)
N,M=map(int,input().split())
cnt=0
ch=[0]*(M)
DFS(0)
print(cnt)
