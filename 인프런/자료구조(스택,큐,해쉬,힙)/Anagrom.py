# Anagram은 두 문자열이 알파벳의 나열 순서를 다르지만 그 구성이 일치하면 두 단어는 아나그램이라고 한다.
first=input()
first=list(map(str,first))
second=input()
second=list(map(str,second))

first.sort()
second.sort()

cnt=0
for i in range(len(first)):
    if first[i]==second[i]:
        cnt=cnt+1
if cnt==len(first):
    print("YES")
else:
    print("NO")