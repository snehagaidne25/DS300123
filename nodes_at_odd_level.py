class newNode:
    def _init_(self, data):
        self.data = data
        self.left = self.right = None
 
def printOddNodes(root, isOdd = True):
     
    if (root == None):
        return
 
    
    if (isOdd):
        print(root.data, end = " ")
 
    
    
    printOddNodes(root.left, not isOdd)
    printOddNodes(root.right, not isOdd)
 
if '_name_' == '_main_':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    printOddNodes(root)