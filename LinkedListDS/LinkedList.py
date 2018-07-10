from Node import Node

class LinkedList(object):
	"""docstring for LinkedList"""
	def __init__(self):
		self.head = None
		self.counter = 0

	def size(self):
		return self.counter

	def insertStart(self, data):
		newNode = Node(data)

		if not self.head:
			self.head = newNode
		else:
			newNode.nextNode = self.head
			self.head = newNode

		self.counter += 1

	def insertEnd(self, data):
		newNode = Node(data)

		if self.head is None:
			self.head = newNode
		else:
			actualNode = self.head

			while actualNode.nextNode is not None:
				actualNode = actualNode.nextNode

			actualNode.nextNode = newNode

		self.counter += 1

	def remove(self, data):
		if self.head:
			if self.head.data == data:
				self.head = self.head.nextNode
			else:
				self.head.nextNode.remove(data, self.head)

	def traverseList(self):
		actualNode = self.head

 		while actualNode is not None:
			print(actualNode.data)
			actualNode = actualNode.nextNode