#Task: Write a Python program to implement a simple stack. (Lists)

def push(stack, element):
    stack.append(element)
    return stack

def pop(stack):
    if len(stack) == 0:
        print("Stack is empty")
    else:
        stack.pop()
        return stack
    
def peek(stack):
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print(stack[-1])
        
def display(stack):
    print(stack)
    
stack = []
push(stack, 1)
push(stack, 2)
push(stack, 3)
push(stack, 4)
push(stack, 5)
display(stack)
pop(stack)
display(stack)
peek(stack)
display(stack)
