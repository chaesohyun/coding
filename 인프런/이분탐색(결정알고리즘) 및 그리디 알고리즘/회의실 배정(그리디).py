# n 개의 회의 수가 입력되고
# 시작, 끝 시간이 입력이 된다.
# 회의를 배치하여 최대의 회의 수 출력

n=int(input())
x=[]
for i in range(n):
    a,b=map(int, input().split())
    x.append((a,b))
x.sort(key=lambda x : (x[1],x[0])) #x[1]이 1순위로 정렬을 함
# x.sort() 그냥 이렇게 하면 튜플의 제일 앞에 의해서 정렬이 됨.

tmp=0
cnt=0
for a,b in x:
    if a>=tmp:
        tmp=b
        cnt=cnt+1
print(cnt)