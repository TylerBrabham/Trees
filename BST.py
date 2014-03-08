

class BST(object):
	root = None
	size = 0

	def __init__(self):
		self.root = None
		self.size = 0

	def insert(self, key):

		if self.root==None:
			self.root = BSTNode(None,None,None,key)

		else:
			prev_node = None
			node = self.root
			while node != None:
				prev_node = node
				if key <= node.key:
					node = node.left_child
				elif key > node.key:
					node = node.right_child

			if key<=prev_node.key:
				prev_node.left_child = BSTNode(prev_node, None,None,key)
			else:
				prev_node.right_child = BSTNode(prev_node, None,None,key)

		self.size += 1

	def find(self, key):
		
		node = self.root

		while node != None:
			if key<node.key:
				node = node.left_child
			elif key>node.key:
				node = node.right_child
			else:
				return node

		return None

	def remove(self, key):
		
		node = self.root
		while node != None:
			if key<node.key:
				node = node.left_child
			elif key>node.key:
				node = node.right_child
			else:
				break

		if node==None:
			return None
		else:
			#find key in right subtree

			if node.left_child==None and node.right_child==None:
				if node.parent!=None:
					if node.parent.left_child==node:
						node.parent.left_child = None
					else:
						node.parent.right_child = None

					node.parent = None
				else:
					self.root = None
			elif node.left_child!=None and node.right_child==None:
				if node.parent!=None:
					if node.parent.left_child==node:
						node.parent.left_child = node.left_child
						node.left_child.parent = node.parent
					else:
						node.parent.right_child = node.left_child
						node.left_child.parent = node.parent
				else:
					self.root = node.left_child
					self.root.parent = None

				node.parent = None
				node.left_child = None

			elif node.right_child!=None and node.left_child==None:
				if node.parent!=None:
					if node.parent.left_child==node:
						node.parent.left_child = node.right_child
						node.right_child.parent = node.parent
					else:
						node.parent.right_child = node.right_child
						node.right_child.parent = node.parent
				else:
					self.root = node.right_child
					self.root.parent = None

				node.right_child = None
				node.parent = None

			else:
				prev_node = None
				replacement = node.right_child

				while replacement!=None:
					prev_node = replacement
					replacement = replacement.left_child

				replacement = prev_node

				self.remove(replacement.key)


				replacement.left_child = node.left_child
				if node.left_child!=None:
					node.left_child.parent = replacement

				replacement.right_child = node.right_child
				if node.right_child!=None:
					node.right_child.parent = replacement

				replacement.parent = node.parent

				if node.parent==None:
					self.root = replacement

				node.parent = None
				node.left_child = None
				node.right_child = None

			self.size -= 1

class BSTNode(object):

	left_child = None
	right_child = None
	parent = None
	key = None

	def __init__(self, parent, lft_child, rgt_child, key_arg):
		self.left_child = lft_child
		self.right_child = rgt_child
		self.parent = parent
		self.key = key_arg

def main():
	test_tree = BST()

	test_tree.insert(5)
	test_tree.insert(4)
	test_tree.insert(100)

	print test_tree.root.key, test_tree.root.left_child.key, test_tree.root.right_child.key
	test_tree.remove(5)
	print test_tree.root.key, test_tree.root.left_child.key
	test_tree.insert(5)
	print test_tree.root.key, test_tree.root.left_child.key, test_tree.root.left_child.right_child.key
	test_tree.remove(4)
	print test_tree.root.key, test_tree.root.left_child.key

	print test_tree.root.left_child.key

	print test_tree.find(4)

	print test_tree.size

if __name__=="__main__":
	main()