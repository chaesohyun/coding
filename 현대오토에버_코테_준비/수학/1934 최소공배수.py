T=int(input())

def gcd(x,y):
    while y:
        x,y=y,x%y
    return x

for i in range(T):
    A,B=map(int, input().split())
    print(int(A*B/gcd(A,B)))