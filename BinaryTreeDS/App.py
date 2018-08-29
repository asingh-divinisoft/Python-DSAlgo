from BinarySearchTree import BST

bst = BST()

bst.insert(12)
bst.insert(10)
bst.insert(-2)
bst.insert(1)

bst.traverseInOrder()

bst.remove(10)

bst.traverseInOrder()

print(bst.getMax())