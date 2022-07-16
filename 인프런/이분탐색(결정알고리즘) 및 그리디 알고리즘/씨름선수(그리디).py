# n명의 씨름 선수 중에서
# 키, 몸무게 중 하나라도 다른 지원자보다 크면 선발이 됨.
# 씨름 선수의 최대 인원 출력

n=int(input())
x=[]
for i in range(n):
    a,b=map(int,input().split())
    x.append((a,b))
# 키 순으로 정렬
x.sort(reverse=True)

cnt=0
tmp=0
for a,b in x:
    if tmp<b:
        tmp=b
        cnt=cnt+1
print(cnt)