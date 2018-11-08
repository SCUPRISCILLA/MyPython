class NLode(object):
	"""docstring for NLode"""
	def __init__(self, x):
		self.data = x
		self.next = None

def DeleteSame(head):
	outtercur = None
	innercur = None
	innerpre = None
	#double loop
	outtercur = head.next

	while outtercur != None:
		innercur = outtercur.next
		innerpre = outtercur
		while innercur != None:
			if innercur.data == innerpre.data:
				innerpre.next = innercur.next
				innercur = innercur.next
			else:
				innerpre = innerpre.next
				innercur = innercur.next
		outtercur = outtercur.next

if __name__ == "__main__":
	head = NLode(1)
	p1 = NLode(1)
	p2 = NLode(1)
	p3 = NLode(4)
	p4 = NLode(3)
	p5 = NLode(2)
	p6 = NLode(2)
	head.next = p1
	p1.next = p2
	p2.next = p3
	p3.next = p4
	p4.next = p5
	p5.next = p6
	p6.next = None
	#make a linked list: 1 1 4 3 2 2
	print("Before: ")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next
	DeleteSame(head)
	print("After: ")
	cur = head.next
	while cur != None:
		print(cur.data)
		cur = cur.next