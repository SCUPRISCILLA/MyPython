class LNode(object):
	"""docstring for LNode"""
	def __init__(self, x):
		self.data = x
		self.next = None

def Deletesame(head):
	outcur = head.next
	inpre = head.next
	incur = inpre.next

	while outcur != None:
		while incur != None:
			if inpre.data == incur.data:
				inpre.next = incur.next
				incur = incur.next
			else:
				inpre = incur
				incur = incur.next
		outcur = outcur.next
	return head

if __name__ == "__main__":
	head = LNode(1)
	p1 = LNode(1)
	p2 = LNode(1)
	p3 = LNode(2)
	p4 = LNode(3)
	p5 = LNode(3)
	head.next = p1
	p1.next = p2
	p2.next = p3
	p3.next = p4
	p4.next = p5
	p5.next = None

	Deletesame(head)
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next