x=input()
dic={"chae":"1","so":"3","hyun":"4"}
for key, value in dic.items():
    x=x.replace(key,value)
print(x)