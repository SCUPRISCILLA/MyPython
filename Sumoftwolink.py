class LNode(object):
	"""docstring for LNode"""
	def __init__(self, x):
		self.data = x
		self.next = None

def Sumtwolink(h1, h2):
	if h1 == None or h1.next == None:
		return h2
	if h2 == None or h2.next == None:
		return h1

	c = 0  
	#carry on jinwei
	sums = 0
	#sum of two linked list
	p1 = h1.next
	p2 = h2.next
	tmp = None
	resHead = LNode(1)
	resHead.next = None
	p = resHead

	while p1 != None and p2 != None:
		tmp = LNode(1)
		tmp.next = None
		sums = p1.data + p2.data + c
		tmp.data = sums%10
		c = sums//10
		sums = 0
		p.next = tmp
		p = tmp
		p1 = p1.next
		p2 = p2.next

	if p1 == None:
		while p2 != None:
			tmp = LNode(1)
			tmp.next = None
			sums = p2.data+c
			tmp.data = sums%10
			c = sums//10
			p.next = tmp
			p = tmp
			p2 = p2.next

	if p2 == None:
		while p1 != None:
			tmp = LNode(1)
			tmp.next = None
			sums = p1.data+c
			tmp.data = sums%10
			c = sums//10
			p.next = tmp
			p = tmp
			p1 = p1.next

	if c != 0:
		tmp = LNode(1)
		tmp.next = None
		tmp.data = 1
		p.next = tmp

	return resHead

if __name__ == "__main__":
	h1 = LNode(1)
	p1 = LNode(1)
	p2 = LNode(9)
	p3 = LNode(3)
	#391

	h2 = LNode(1)
	p4 = LNode(3)
	p5 = LNode(2)
	p6 = LNode(1)
	p7 = LNode(7)
	#7123
	h1.next = p1
	p1.next = p2
	p2.next = p3
	p3.next = None

	h2.next = p4
	p4.next = p5
	p5.next = p6
	p6.next = p7
	p7.next = None

	res = Sumtwolink(h1, h2)
	cur = res.next
	while cur != None:
		print(cur.data)
		cur = cur.next