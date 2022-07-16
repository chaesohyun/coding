# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
# p와 q가 있을 때, p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다.
# N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.

def K_yaksu(N, K):
    count=0
    for i in range(1,int(N)):
        if int(N)%i==0:
            count=count+1
            if count==int(K):
                return i






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    N,K=input().split()
    print(K_yaksu(N,K))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
