class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    currentNode = linkedList
    while currentNode != None:
        nextNode = currentNode.next
        while nextNode is not None and nextNode.value == currentNode.value:
            nextNode = nextNode.next
        currentNode.next = nextNode
        currentNode = nextNode
    print(linkedList)
    return linkedList


linked_lst = LinkedList(1)
linked_lst.next = LinkedList(1)
linked_lst.next = LinkedList(2)

removeDuplicatesFromLinkedList(linked_lst)
