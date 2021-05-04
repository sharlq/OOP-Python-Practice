# the only conection usally between elements in the array that they are next to each other in memory
# the linked list has no strict linear ordering in memory istead the ordering of teh elements controlled by the datastructure which contain each one of the indivisual elements
# rather than each element having its fixed size bloch in memory slotted in next to its neighors the linked list uses a data structure called a node to wrap each one of its elements 
# along wiht the node it self this node structure contain the metadata that show the whole  linked list togather 
# the node contain for one a pointer for teh next element in the list you can think of the pointer as the memory adress of the next node or the next node it self
# it has the knowladge of how to get to the next node
# finidng element takes O(n)
# remove last element in single list O(n) in double O(1)

# differences between it and array
# 1- its dynamic
# 2- its sequential access where the array can be direct using index or random
# 3- we cant use binary search on the linked list 

class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class Linked_List:
    def __init__(self):
        self.head = Node() # place holder to point for the first element in the list
     
    def append(self,data):
        new_node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next=new_node

    def length(self):
        current = self.head
        total = 0
        while current.next!=None:
            total+=1
            current=current.next
        return total

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next  != None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)


my_list = Linked_List()

my_list.append(1)
my_list.display()