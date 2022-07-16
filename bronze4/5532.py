L=int(input())
A=int(input())
B=int(input())
C=int(input())
D=int(input())

if int(A/C) < A/C:
    x=int(A/C)+1
else:
    x=int(A/C)

if int(B/D) < B/D:
    y=int(B/D)+1
else:
    y=int(B/D)
print(L-max(x,y))