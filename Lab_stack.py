class Stack:
    def __init__(self):
        self.item = []

    def push(self, item):
        return self.item.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.item.pop(-1)

    def peek(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.item[-1]

    def is_empty(self):
        if len(self.item) == 0:
            return True

    def size(self):
        return len(self.item)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print("Size  after push:", s.size())
print("Top element:", s.peek())


print("Pop", s.pop())
print("Pop", s.pop())
print("Pop", s.pop())
print("Pop", s.pop())
print("Pop", s.pop())

print("Is empty?", s.is_empty())
print("Pop from empty:", s.pop())


