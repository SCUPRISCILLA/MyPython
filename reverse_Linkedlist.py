class LNode(object):
	"""docstring for LNode"""
	def __init__(self, x):
		self.data = x
		self.next = None

def Reverse(head):
	if head == None or head.next == None:
		return
	pre = None
	cur = None
	next = None

	cur = head.next
	next = cur.next
	cur.next = None
	pre = cur
	cur = next

	while cur.next != None:
		next = cur.next
		cur.next = pre
		pre = cur
		cur = next

	cur.next = pre
	head.next = cur

if __name__ == "__main__":
	i = 1
	head = LNode(1)
	tmp = None
	cur = head

	while i<8:
		tmp = LNode(i)
		tmp.data = i
		tmp.next = None
		cur.next = tmp
		cur = tmp
		i += 1
	#build a linked list

	print("Before: ")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next

	print("After: ")
	Reverse(head)
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next
		