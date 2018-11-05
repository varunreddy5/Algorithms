class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    # def __len__(self):
    #     return self.size()

    def size(self):
        return len(self.items)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)
        else:
            print("Traversal type " + str(traversal_type) + " is not supported")

    def preorder_print(self, start, traversal):
        #Root -> Left -> Right
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        #Left -> Root -> Right
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = traversal + str(start.value) + "-"
            traversal = self.inorder_print(start.right, traversal)
        return traversal
    def postorder_print(self, start, traversal):
        # Left -> Right -> Root
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal = traversal + str(start.value) + "-"
        return traversal

    def levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)
        traversal = ""
        while queue.size() > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1+max(left_height, right_height)
    def height_iterative(self, node):
        queue = []
        queue.insert(0, node)
        height = -1
        result = []
        while queue:
            length_queue = len(queue)
            while length_queue > 0:
                node = queue.pop()
                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)
                length_queue-=1
            height += 1
        return height
    def size_iterative(self):
        if self.root is None:
            return 0
        stack = []
        size = 1
        stack.append(self.root)
        while stack:
            node = stack.pop()
            if node.left:
                size+=1
                stack.append(node.left)
            if node.right:
                size+=1
                stack.append(node.right)
        return size
    def size_recursive(self, node):
        if node is None:
            return 0
        return 1  + self.size_recursive(node.left) + self.size_recursive(node.right)





#Set up the tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
# tree.root.right.left = Node(6)
# tree.root.right.right = Node(7)
print(tree.print_tree("levelorder"))
print(tree.height(tree.root))
print(tree.height_iterative(tree.root))
print(tree.size_iterative())
print(tree.size_recursive(tree.root))
