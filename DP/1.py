# 7개의 원소의 합이 100인 경우를 찾아야 함.

num=[]
for i in range(9):
    n=int(input())
    num.append(n)
# 2개의 원소의 합이 100-sum 나오는 것 찾으면 됨.
total=sum(num)
for i in range(9):
    for j in range(i+1,9):
        if 100==total-(num[i]+num[j]):
            num1,num2=num[i],num[j]

            num.remove(num1)
            num.remove(num2)
            num.sort()

            for i in range(len(num)):
                print(num[i])
            break

    # if len(num)<9:
    #     break
