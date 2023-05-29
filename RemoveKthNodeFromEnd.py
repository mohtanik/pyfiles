class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
	first = head
	second = head
	
	for i in range(0,k):
		second = second.next
	
	if second is None:
		head.value = head.next.value
		head.next = head.next.next
		return
		
	while second.next!=None:
		first = first.next
		second=second.next
	
	first.next = first.next.next
