a_bg=int(input())
b_bg=int(input())
c_bg=int(input())
coke=int(input())
saida=int(input())

bg=[a_bg,b_bg,c_bg]
drink=[coke,saida]
x=[]
for i in range(3):
    for j in range(2):
        x.append(bg[i]+drink[j]-50)
print(min(x))