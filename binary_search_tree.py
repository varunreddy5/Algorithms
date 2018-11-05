class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Duplicate values are not allowed")

    def find(self, data):
        if self.root is None:
            return None
        else:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
    def _find(self, data, cur_node):
        if data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        elif data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        if data == cur_node.data:
            return True
    def inorder_print(self):
        #Left -> Root -> Right
        if self.root:
            self._inorder_print(self.root)
    def _inorder_print(self, cur_node):
        if cur_node:
            self._inorder_print(cur_node.left)
            print(str(cur_node.data))
            self._inorder_print(cur_node.right)

    def is_bst_satisfied(self):
        if self.root:
            is_satisfied = self._is_bst_satisfied(self.root, self.root.data)
            if is_satisfied is None:
                return True
            return False
        return True

    def _is_bst_satisfied(self, cur_node, data):
        if cur_node.left:
            if data > cur_node.left.data:
                self._is_bst_satisfied(cur_node.left, cur_node.data)
            else:
                return False
        if cur_node.right:
            if data < cur_node.right.data:
                self._is_bst_satisfied(cur_node.left, cur_node.data)
            else:
                return False

bst = BST()
bst.insert(5)
bst.insert(4)
bst.insert(6)
bst.insert(3)
bst.insert(7)
print(bst.find(4))
print(bst.is_bst_satisfied())
