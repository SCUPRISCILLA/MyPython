class NLode(object):
	"""docstring for NLode"""
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
	#destroy head.next.next in order to inverse

	while cur.next != None:
		next = cur.next
		cur.next = pre
		pre = cur
		cur = next

	cur.next = pre
	head.next = cur


def MakeList(num):
	head = NLode(1)
	cur = head
	tmp = None
	i = 1
	while i<=num:
		tmp = NLode(i)
		tmp.data = i
		tmp.next = None
		cur.next = tmp
		cur = tmp
		i += 1
	return head


if __name__ == "__main__":
	head = MakeList(5)
	print("Before:")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next

	print("After:")
	Reverse(head)
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next	




		