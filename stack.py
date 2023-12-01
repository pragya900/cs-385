class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty.")

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Queue is empty.")

    def front(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Queue is empty.")

    def size(self):
        return len(self.items)


# Example usage
if __name__ == "__main__":
    # Stack
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack:")
    print("Peek:", stack.peek())
    print("Pop:", stack.pop())
    print("Peek after Pop:", stack.peek())
    print("Size:", stack.size())

    print("\n")

    # Queue
    queue = Queue()
    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')

    print("Queue:")
    print("Front:", queue.front())
    print("Dequeue:", queue.dequeue())
    print("Front after Dequeue:", queue.front())
    print("Size:", queue.size())
