from Node import Node
import math

class BalancedTree(object):
	"""docstring for BalancedTree"""
	def __init__(self):
		self.rootNode = None

	def insert(self, data):
		if self.rootNode is None:
			self.rootNode = Node(data, None)
			parentNode = self.rootNode
		else:
			parentNode = self.rootNode.insert(data)

		self.rebalanceTree(parentNode)

	def rebalanceTree(self, node):
		self.setBalance(node)

		if node.parentNode is not None:
			self.rebalanceTree(node.parentNode)

	def setBalance(self, node):
		node.balance = self.height(node.rightChild) - self.height(node.leftChild)

		if node.balance > 1:
			if node.rightChild.balance < 0:
				self.rotateright(node.rightChild.leftChild)
			self.rotateleft(node.rightChild)

		if node.balance < -1:
			if node.leftChild.balance > 0:
				self.rotateleft(node.leftChild.rightChild)
			self.rotateright(node.leftChild)

	def rotateleft(self, node):
		son = node.leftChild
		parent = node.parentNode
		grand_parent = node.parentNode.parentNode
		node.leftChild = parent
		node.parentNode = grand_parent
		parent.rightChild = son
		parent.parentNode = node
		if son:
			son.parentNode = parent
		if grand_parent:
			if parent == grand_parent.rightChild:
				grand_parent.rightChild = node
			else:
				grand_parent.leftChild = node
		else:
			self.rootNode = node

	def rotateright(self, node):
		son = node.rightChild
		parent = node.parentNode
		grand_parent = node.parentNode.parentNode
		node.rightChild = parent
		node.parentNode = grand_parent
		parent.leftChild = son
		parent.parentNode = node
		if son:
			son.parentNode = parent
		if grand_parent:
			if parent == grand_parent.rightChild:
				grand_parent.rightChild = node
			else:
				grand_parent.leftChild = node
		else:
			self.rootNode = node

	def height(self, node):
		if node == None:
			return -1
		else:
			return 1 + max(self.height(node.leftChild), self.height(node.rightChild))

	def traverseInOrder(self):
		if self.rootNode is not None:
			self.rootNode.traverseInOrder()