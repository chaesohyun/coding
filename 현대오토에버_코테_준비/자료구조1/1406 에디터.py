import sys
s=input()
stack=list(s)
M=int(input())
w=len(stack)
for i in range(M):
    command=sys.stdin.readline().split()

    if command[0]=='P':
        stack.insert(w,command[1])
        w=w+1
    elif command[0]=='L':
        w=w-1
    elif command[0]=='D':
        w=w+1
    elif command[0]=='B':
        del stack[w-1]
        w=w-1
print(''.join(stack))


