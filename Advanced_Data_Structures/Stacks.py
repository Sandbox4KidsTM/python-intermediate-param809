# -*- coding: utf-8 -*-




class My_Stack():
    def __init__(self):
        self._stack =[]
        
        def __repr__(self):
           a = ", ".join(str(x) for x in self._stack.reverse)
            
        
    def push(self, item):
        self._stack.append()
    
    def pop(self):
        return self._pop()
    
    def peek(self):
        return self._stack[-1]
    
stack = My_Stack()
stack.push("Red")
stack.push("Green")
stack.push("Blue")

print(stack.peek() == "Blue")
print(stack.pop() == "Blue")
print(stack)