class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def FindLargestValue(head):
    maxValue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data > maxValue:
            maxValue = currentNode.data
        currentNode = currentNode.next
    return maxValue


node1 = Node(30)
node2 = Node(50)
node3 = Node(120)
node4 = Node(5)
node5 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None

print("The largest node is ", FindLargestValue(node1))



    