X=int(input())
Y=int(input())
C=int(input())
D=int(input())
P=int(input())

res_x=X*P
if P>C:
    res_y=Y+(P-C)*D

else:
    res_y=Y

print(min(res_x,res_y))