class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty."

    def is_empty(self):
        return len(self.items) == 0

    def __iter__(self):
        return StackIterator(self)

class StackIterator:
    def __init__(self, stack):
        self.stack = stack
        self.index = len(stack.items) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            item = self.stack.items[self.index]
            self.index -= 1
            return item
        else:
            raise StopIteration

stack = Stack()
num_elements = int(input("Enter the number of elements to push onto the stack: "))

for i in range(num_elements):
    element = input(f"Enter element {i + 1}: ")
    stack.push(element)

print("Popping elements from the stack in LIFO order:")
for item in stack:
    print(item)

