# 필수과목 순서 CBA가 주어지면 B는 C를 듣고 들을 수 있음

### 스택으로 푼 내 풀이
# arr=input()
# arr=list(map(str, arr))
# N=int(input())
# cnt=0
# for i in range(N):
#     cnt=cnt+1
#     x=input()
#     x=list(map(str,x))
#     stack=[]
#     for i in x:
#         if i in arr and i not in stack:
#             stack.append(i)
#     print(stack)
#     if arr==stack:
#         print("#",cnt," YES")
#     else:
#         print("#",cnt," NO")

## 큐로 푼 선생님 풀이
from collections import deque
need=input()
N=int(input())
for i in range(N):
    plan=input()
    dq=deque(need)
    for j in plan:
        if j in dq:
            if dq.popleft()!=j:
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" % (i+1))
