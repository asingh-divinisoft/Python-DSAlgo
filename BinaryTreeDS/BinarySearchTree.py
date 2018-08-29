from Node import Node

class BST(object):

	def __init__(self):
		self.rootNode = None

	def insert(self, data):
		if not self.rootNode:
			self.rootNode = Node(data)
		else:
			self.rootNode.insert(data)

	def remove(self, data):
		if self.rootNode is not None:
			if self.rootNode.data == data:
				tempNode = Node(None)
				tempNode.leftchild = self.rootNode
				self.rootNode.remove(data, tempNode)
			else:
				self.rootNode.remove(data, None)

	def getMax(self):
		if self.rootNode is not None:
			return self.rootNode.getMax()

	def getMin(self):
		if self.rootNode is not None:
			return self.rootNode.getMin()

	def traverseInOrder(self):
		if self.rootNode is not None:
			self.rootNode.traverseInOrder()
