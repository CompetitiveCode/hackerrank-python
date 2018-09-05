#Answer to Day 18: Queues and Stacks

from collections import deque
class Solution:
    def __init__(self):
        self.stack = deque()
        self.queue = deque()
    def pushCharacter(self,val):
        self.stack.append(val)
    def enqueueCharacter(self,val):
        self.queue.append(val)
    def popCharacter(self):
        return self.stack.pop()
    def dequeueCharacter(self):
        return self.queue.popleft()