# 첫 줄에 자연수 N과 K가 입력되고, N개의 카드값이 입력된다.
# 첫 줄에 K 번째 수를 출력한다.

if __name__ == '__main__':
    N,K=map(int, input().split())
    number=list(map(int, input().split()))
    x=[]
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                x.append(number[i]+number[j]+number[k])

    x.sort(reverse=True)
    print(x[K-1])