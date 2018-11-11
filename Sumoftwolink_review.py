class LNode(object):
	"""docstring for LNode"""
	def __init__(self, x):
		self.data = x
		self.next = None

def Addtwolist(h1, h2):  #h1 is list1's head, h2 is list2's head
	if h1 == None or h1.next == None:
		return h2
	if h2 == None or h2.next == None:
		return h1
		
	c = 0
	reshead = LNode(1)  #final result
	reshead.next = None
	p = reshead
	p1 = h1.next
	p2 = h2.next

	while p1 != None and p2 != None:
		tmp = LNode(1)  #tmp
		tmp.next = None
		tmp.data = (p1.data+p2.data+c)%10
		c = (p1.data+p2.data+c)//10
		p.next = tmp
		p = p.next
		p1 = p1.next
		p2 = p2.next

	if p1 != None:
		tmp = LNode(1)  #tmp
		tmp.next = None
		tmp.data = (p1.data+c)%10
		c = (p1.data+c)//10
		p.next = tmp
		p = p.next
		p1 = p1.next

	if p2 != None:
		tmp = LNode(1)  #tmp
		tmp.next = None
		tmp.data = (p2.data+c)%10
		c = (p2.data+c)//10
		p.next = tmp
		p = p.next
		p2 = p2.next

	return reshead

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

	res = Addtwolist(h1, h2)
	cur = res.next
	while cur != None:
		print(cur.data)
		cur = cur.next





