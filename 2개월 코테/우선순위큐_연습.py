from queue import PriorityQueue

pq=PriorityQueue()
pq.put(123)
pq.put(345)
pq.put(320)
print(pq.get())
while not pq.empty():
    print(pq.get())