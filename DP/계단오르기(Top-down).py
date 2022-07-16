# 철수가 계단을 오를 때 한 번에 한 계단 도는 두 계단씩 올라간다.
# 만약 총 4계단을 오른다면 그 방법의 수는 (1,1,1,1) (1,1,2) (1,2,1) (2,1,1) (2,2) 5가지 이다.
# N 계단일 때 올라갈 수 있는 방법으 ㅣ수는?
def DFS(N):
    if N==1:
        return 1
    elif N==2:
        return 2
    else:
        return DFS(N-1)+DFS(N-2)
if __name__=='__main__':
    N=int(input())
    print(DFS(N))