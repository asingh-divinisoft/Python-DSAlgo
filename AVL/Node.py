class Node(object):
	def __init__(self, data, parentNode):
		self.data = data
		self.parentNode = parentNode
		self.leftChild = None
		self.rightChild = None
		self.balance = 0

	def insert(self, data):
		
		if data < self.data:
			if self.leftChild is None:
				self.leftChild = Node(data, self)
				return self
			else:
				return self.leftChild.insert(data)
		else:
			if self.rightChild is None:
				self.rightChild = Node(data, self)
				return self
			else:
				return self.rightChild.insert(data)

	def traverseInOrder(self):
		if self.leftChild is not None:
			self.leftChild.traverseInOrder()

		print(self.data)

		if self.rightChild is not None:
			self.rightChild.traverseInOrder()

	def getMax(self):
		if self.rightChild is not None:
			self.rightChild.getMax()
		else:
			return self.data

	def getMin(self):
		if self.leftChild is not None:
			self.leftChild.getMin()
		else:
			return self.data