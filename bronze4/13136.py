R,C,N=map(int, input().split())
if int(R/N)<R/N:
    x=int(R/N)+1
else:
    x=int(R/N)

if int(C/N)<C/N:
    y=int(C/N)+1
else:
    y=int(C/N)

print(x*y)