# 정수를 저장하는 스택
# 명령 5가지 push X, pop, size, empty, top

# 입력 - 명령의 수 N
import sys
N=int(sys.stdin.readline())
stack=[]
for i in range(N):
    command=sys.stdin.readline().split()

    if command[0]=='push':
        stack.append(command[1])

    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())

    elif command[0]=='size':
        print(len(stack))

    elif command[0] =='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)

    elif command[0] =='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
# 출력 - 명령이 주어질 때마다 하나씩 출력
