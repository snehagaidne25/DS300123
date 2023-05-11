count = 0;
   
# Structure of a Node of binary tree
class Node:
    def _init_(self):
        self.data = 0;
        self.left = None;
        self.right = None;
 
# Function to get a new Node
def getNode(data):
   
    # Allocate space
    newNode = Node();
 
    # Put in the data
    newNode.data = data;
    newNode.left = newNode.right = None;
    return newNode;
 
# Function to find digit sum of number
def digitSum(N):
    sum = 0;
    while (N > 0):
        sum += N % 10;
        N //= 10;
     
    return sum;
 
# Function to replace all the Nodes
# with their digit sums using pre-order
def replaceNodes(root):
    if (root == None):
        return;
 
    # Assigning digit sum value
    root.data = digitSum(root.data);
 
    # Calling left sub-tree
    replaceNodes(root.left);
 
    # Calling right sub-tree
    replaceNodes(root.right);
 
 
# Function to count subtrees that
# Sum up to a given value x
def countSubtreesWithSumX(root, x):
   
    # If tree is empty
    if (root == None):
        return 0;
 
    # Sum of Nodes in the left subtree
    ls = countSubtreesWithSumX(root.left,  x);
 
    # Sum of Nodes in the right subtree
    rs = countSubtreesWithSumX(root.right,  x);
 
    # Sum of Nodes in the subtree rooted
    # with 'root.data'
    sum = ls + rs + root.data;
 
    # If True
    if (sum == x):
        count += 1;
 
    # Return subtree's Nodes sum
    return sum;
 
 
def countSubtreesWithSumXUtil(root, x):
   
    
    if (root == None):
        return 0;
 
    count = 0;

    ls = countSubtreesWithSumX(root.left,  x);
 
    rs = countSubtreesWithSumX(root.right,  x);
 
    
    if ((ls + rs + root.data) == x):
        count+=1;
 
    
    return count;
 

if '_name_' == '_main_':
    N = 7;
    root = getNode(10);
    root.left = getNode(2);
    root.right = getNode(3);
    root.left.left = getNode(9);
    root.left.right = getNode(3);
    root.right.left = getNode(4);
    root.right.right = getNode(7);
 
    replaceNodes(root);
 
    X = 29;
 
    print(countSubtreesWithSumXUtil(root, X));