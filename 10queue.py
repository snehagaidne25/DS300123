def createStack():
    stack = []
    return stack
  
# Stack is empty when stack size is 0
def isEmpty(stack):
    return len(stack) == 0
  

def push(stack, item):
    stack.append(item)
    print(item + " pushed to stack ")
      

def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize -1) 
      
    return stack.pop()
  

def peek(stack):
    if (isEmpty(stack)):
        return str(-maxsize -1) 
    return stack[len(stack) - 1]
  
# Driver program to test above functions    
stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print(pop(stack) + " popped from stack")