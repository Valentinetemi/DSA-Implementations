class Node: #This is a blueprint for creating a node
    def __init__(self, data):
        self.data = data # This is the data that stores the node and the self is the object that stores the data
        self.next = None #This is the one that point to the last node and say iti is null
        
def traverseAndPrint(head):
    currentNode = head # This is the first node and the head is the first node
    while currentNode:#This is a while loop that print the data of the current node
        print(currentNode.data, end="-->") ##This print the nodes with a --> pointer, pointing to the next node
        currentNode = currentNode.next #This point the current node to the next node
    print("None") #This print it
    
#This is to store the  node as this numbers and create  them separately 
node1 = Node(8) 
node2 = Node(6)
node3 = Node(30)
node4 = Node(12)
node5 = Node(10)

#This is are to point the nodes to the next one and connect the nodes together

node1.next = node3 
node2.next = node3
node3.next = node4
node4.next = node5

traverseAndPrint(node1) #call the function and print the node

        
