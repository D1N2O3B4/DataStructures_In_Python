class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None


def printList(self):
    temp = self.head
    while(temp):
        print(temp.data,end=",")
        temp = temp.next

lisp = LinkedList()
lisp.head = Node(10)
second = Node(11)
third = Node(12)

lisp.head.next = second
second.next = third

printList(lisp)