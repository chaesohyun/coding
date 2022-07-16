# 2186

if __name__ == '__main__':
    N,M,K=map(int,input().split())

    pan=[]
    for i in range(N):
        x=str(input())
        pan.append(x)

    q=[]
    for i in range(N):
        q.append([])
        for j in range(M):
            q[i].append(pan[i][j])

    word=list(map(str,input().split()))


    # 첫 문자 찾기
    first_index=[]
    for i in range(N):
        for j in range(M):
            if q[i][j]==word[0][0]:
                first_index.append([i,j])

    # 다음 단어 찾기

    for i in 