class MinHeap():
    def __init__(self,capacity):
        self.storage=[0]*capacity
        self.capacity = capacity
        self.size = 0

    # find the element
    def getParentIndex(self,index):
        return (index-1)//2
    def getLeftChildIndex(self,index):
        return 2*index+1
    def getRightChildIndex(self,index):
        return 2*index+2
    
    # check if the element exist
    def hasParent(self,index):
        return self.getParentIndex(index) >= 0
    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index) < self.size
    def hasRightChild(self,index):
        return self.getRightChildIndex(index) < self.size # size is tha number of elements in teh heap sice we are using sorted array to create the heape by arranging the indexes of the array means that in the index of the child is less than the size means it exist 
    
    # get the elemnt
    def parent(self,index):
        return self.storage[self.getParentIndex(index)]
    def leftChild(self,index):
        return self.storage[self.getLeftChildIndex(index)]
    def rightChild(self,index):
        return self.storage[self.getRightChildIndex(index)]

    # to check if we can insert to the heap
    def isFull(self):
     return self.size== self.capacity

    # re heapfy the heap 
     def swap(self,index1,index2):
        self.storage[index1],self.storage[index2]=self.storage[index2],self.storage[index1]
    def heapifyUp(self):
        index = self.size -1
        while(self.hasParent(index)and self.parent(index)>self.storage[index]):
            self.swap(self.getParentIndex(index),index)
            index = self.getParentIndex(index)


    #insert to the heap 
    def insert(self,data):
        if(self.isFull()):
            raise("Heap is Full")
        self.storage[self.size]=data
        self.size +=1
        self.heapifyUp()


# note we reach the parent and the left child and teh right child using one index