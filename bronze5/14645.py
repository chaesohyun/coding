# N 정거장 수 , K 출발역에서 타는 사람 수
N,K=map(int,input().split())
for i in range(N):
    A,B=map(int, input().split())
    if i==N-1:
        print("비와이")