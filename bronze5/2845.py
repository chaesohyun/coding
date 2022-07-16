L,P=map(int, input().split())
num=list(map(int, input().split()))
std=L*P
for i in num:
    print(i-std,end=' ')