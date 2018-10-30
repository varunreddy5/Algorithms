class Queue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        return self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def get_queue(self):
        return self.items

    def size(self):
        return len(self.items)

q= Queue()
q.enqueue(3)
q.enqueue(5)
q.enqueue(8)
print(q.size())
q.dequeue()
print(q.get_queue())
