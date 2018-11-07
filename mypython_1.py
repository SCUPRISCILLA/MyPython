class LNode:
	def __new__(self, x):
		self.data = x
		self.next = None

def Reverse(head):
	if head == None or head.next == None:
		
		