a=[1,2,3,4,5,5,5]

#5가 1개만 제거가 됨
a.remove(5)
print(a)

#집합을 이용해서 모두 제거할 수 있는 방법
b=[1,2,3,4,5,5,5,4]
remove_set={4,5}
x=[i for i in b if i not in remove_set]
print(x)
