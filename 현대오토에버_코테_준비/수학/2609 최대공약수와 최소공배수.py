A,B=map(int, input().split())

# 최대공약수 res
# 유클리드 호제법 사용
def gcd(x,y):
    while y!=0:
        x,y=y,x%y
    return x
res=gcd(A,B)
print(res)
# 최소공배수 = A X B / 최대공약수
print(int(A*B/res))