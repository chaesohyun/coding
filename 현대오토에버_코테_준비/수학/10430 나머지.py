
# 입력
import sys
x=sys.stdin.readline().split()
A=int(x[0])
B=int(x[1])
C=int(x[2])
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)