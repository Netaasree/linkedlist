class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=Node(11)
node2=Node(12)
node3=Node(13)
node4=Node(14)

node1.next=node2
node2.next=node3
node3.next=node4
currentnode=node1
while currentnode:
    print(currentnode.data,end="->")
    currentnode=currentnode.next
print("Null")
    

