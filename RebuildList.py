class LNode(object):
	"""docstring for LNode"""
	def __init__(self, x):
		self.data = x
		self.next = None

def FindMid(head):
	if head != None or head.next != None:
		fast = head
		slow = head
		slowpre = None

	while fast != None:	
		fast = fast.next.next
		slowpre = slow
		slow = slow.next
	slowpre.next = None
	return slow

def Reverse(head):
	cur = head.next
	next = cur.next
	cur.next = None
	pre = cur
	cur = next
	next = cur.next

	while cur != None:
		cur.next = pre
		pre = cur
		cur = next
		if cur != None:
			next = cur.next

	head.next = pre
	return head

def Rebuild(head):
	mid = FindMid(head)
	sec = Reverse(mid)
	cur = head.next
	while cur.next != None:
		curnext = cur.next
		secnext = sec.next
		cur.next = sec
		cur = curnext
		sec.next = cur
		sec = secnext
	cur.next = sec

	return head

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
	head = Rebuild(head)
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next


