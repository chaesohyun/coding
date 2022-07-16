
# 테스트 케이스의 수 T
# (N, s, e, k)
# N개의 숫자로 이루어진 숫자열에서 s번째부터 e번째 까지의 수를 오름차순하였을 때, k번째로 나타나는 숫자를 출력

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N, s, e, k = map(int, input().split())
        number=list(map(int, input().split()))
        x=number[s-1:e]
        x.sort()
        print("#%d %d" %(i+1, x[k-1]))


