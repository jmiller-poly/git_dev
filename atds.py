#!/usr/bin/env python3
"""
Advanced Topics Data Structure

This file will be added to over the course of the semester
"""

__author__ = "James Miller"
__version__ = "2/14/23"

class Stack(object):
    """
    Uses lists to construct a stack class
    """
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def __repr__(self):
        return super().__repr__() + str(self.stack)

class Queue(object):
    """
    Uses lists to construct a queue class
    """

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)
    
    def peek(self):
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

    def __repr__(self):
        return str(self.queue)

class Dequeue():
    def __init__(self):
        self.queue = []

    def add_front(self, item):
        self.queue.insert(0, item)

    def add_rear(self, item):
        self.queue.append(item)

    def remove_front(self):
        return self.queue.pop(0)

    def remove_rear(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def __repr__(self):
        return super().__repr__() + str(self.queue)



def main():
    q = Queue()
    q.enqueue("Hello")
    q.enqueue("Goodbye")
    print(q.is_empty())
    print(q.peek())
    print(q.size())
    print(q.dequeue())
    print(q.size())
    print(q.is_empty())
    print(q.dequeue())
    print(q.is_empty())

if __name__ == "__main__":
    main()
