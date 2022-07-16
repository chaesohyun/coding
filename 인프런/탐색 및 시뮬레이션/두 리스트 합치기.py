# 오름차순 정렬된 두 개의 리스트 주어지면 오름차순으로 합쳐 출력

N=int(input())
a=list(map(int, input().split()))
M=int(input())
b=list(map(int,input().split()))

for i in range(M):
    a.append(b[i])

a.sort()
print(a)