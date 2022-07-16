# 재귀, 메모이제이션
# 1,2m로 네트워크 선 자르기 방법 구하기

def DFS(len):
    # 메모이제이션
    # 기록! -> DP
    if dy[len]>0:
        return dy[len]
    if len==1 or len==2:
        return len
    else:
        dy[len]=DFS(len-1)+DFS(len-2)
        return dy[len]

if __name__ =='__main__':
    # n 길이 선이 주어지면 1 또는 2m로 나누는 방법의 수 구하기
    n=int(input())
    dy=[0]*(n+1)
    print(DFS(n))
