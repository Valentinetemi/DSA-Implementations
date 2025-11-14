class Node:
    def __init__(self, data):
        self.data = data # this is the node and the self eis the object that stores the data
        self.next = next #this is the pointer or reference pointing to the next node
        
class LinkedList:
    def __init__(self):
        self.head = None
        
        def insert_at_beginning(self, data):
            node = Node(data, self.head)
            self.head = node
            
        def print(self):
            if self.head is None:
                print("Linked list is empty")
                
            itr
                
                
if __name__ == "__main__":
    pass