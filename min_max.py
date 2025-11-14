#Find the largest node and smallest node in a linked  list node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def FindSmallestValue(head):
    if not head:
        return None
    
    minValue = head.data
    currentNode = head
    
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    return minValue
    
def FindLargestValue(head):
    
    if not head: 
        return None
    
    
    maxValue = head.data
    currentNode = head
    
    while currentNode:
        if currentNode.data > maxValue:
            maxValue = currentNode.data
        currentNode= currentNode.next
    return maxValue
    
node1 = Node(20)
node2 = Node(10)
node3 = Node(25)

node1.next = node2
node2.next = node3
node3.next = None

print("The smallest node is ", FindSmallestValue(node1))
print("The largest Node is ", FindLargestValue(node1))