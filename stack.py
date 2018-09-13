class Stack():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    def size(self):
        return len(self.items)
    def get_stack(self):
        return self.items
s = Stack()
s.push("One")
s.push("Three")
print(s.get_stack())
