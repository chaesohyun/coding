from queue import Queue

q=Queue()
q.put(123)
q.put(456)
print(q.get())
q.put(789)
print(q.get())

while not q.empty():
    print(q.get())
