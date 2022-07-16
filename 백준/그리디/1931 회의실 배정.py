# 1개의 회의실을 사용하고자 하는 N개의 회의에 대한 사용표
# 각 회의의 시작, 끝 시간이 주어지고
# 겹치지 않게 하며 회의실을 사용할 수 있는 최의의 최대 갯수 구하기
### 회의가 끝나는 시간을 기준으로 정렬
### (1,4) (2,3) (3,5) (4,6) (5,7) 이면 (2,3)(1,4)(3,5)(4,6)(5,7) 로 정렬 우선

N=int(input())

tmp=[]
for i in range(N):
    start, end=map(int, input().split())
    tmp.append((start,end))
tmp.sort(key=lambda x:(x[1],x[0]))

x=0
cnt=0
for a, b in tmp:
    if a>=x:
        x=b
        cnt+=1

print(cnt)