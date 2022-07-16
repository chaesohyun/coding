a=int(input())
b=int(input())
c=int(input())

if a+b+c!=180:
    print('Error')
elif a==60 and b==60 and c==60:
    print('Equilateral')
elif (a==b and b!=c) or (a==c and a!=b) or (b==c and a!=b) :
    print('Isosceles')
elif a!=b and b!=c :
    print('Scalene')