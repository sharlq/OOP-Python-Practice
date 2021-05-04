# the averge time complexuty in the binary tree is O(logn) and teh worst is O(n)
# the array is better thatn the binary tree just in the access where its speed access equals O(1) and thats of the binary tree equals O(logn)

class Node:
    def __init__(self,value=None):
        self.value=value
        self.leftChild=None
        self.rightChild=None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,value):
        if self.root==None:
            self.root=Node(value)
        else:
            self._insert(value,self.root)

    def _insert(self,value,currentNode):
        
        if currentNode and currentNode.value > value:
            if currentNode==None:
               currentNode.leftChild=Node(value)
            else:
               self._insert(value,currentNode.rightChild)
        elif currentNode and value>currentNode.value:
            if currentNode.rightChild==None:
                currentNode.rightChild=Node(value)
            else:
                self._insert(value,currentNode.rightChild)

        else:
           print("already in the tree")

    def printTree(self):
        if self.root != Node:
          self._printTree(self.root)
	
    def _printTree(self,currentNode):
        if currentNode!=None:
            self._printTree(currentNode.leftChild)
            print(currentNode.value)
            self._printTree(currentNode.rightChild)
    def height(self):
        if self.root!=None:
            return self._height(self.root,0)
        else:
           return 0
    def _height(self,currentNode,currentHeight):
        if currentNode==None: return currentHeight
        left_height=self._height(currentNode.leftChild, currentHeight+1)
        right_height=self._height(currentNode.rightChild, currentHeight+1)
        return max(left_height,right_height)
    
    def search(self,value):
        if self.root!=None:
            return self._search(value,self.root)
        else:
            return False

    def _search(self,value,currentNode):
        if value == currentNode:
            return True
        elif  value<currentNode.value and currentNode.leftChild!=None:
           return self._search(value,currentNode.leftChild)
        elif  value>currentNode.value and currentNode.rightChild!=None:
           return self._search(value,currentNode.rightChild)
        return False


def fillTree(tree,numElems=100,maxInt=1000):
	from random import randint
	for _ in range(numElems):
		currentElem=randint(0, maxInt)
		tree.insert(currentElem)
	return tree


tree = BinarySearchTree()
tree.insert(0)
tree.insert(5)
tree.insert(12)
tree.insert(7)
tree.insert(6)
tree.insert(4)
tree.insert(9)
tree.insert(10)

tree.printTree()
print(tree.search(0))