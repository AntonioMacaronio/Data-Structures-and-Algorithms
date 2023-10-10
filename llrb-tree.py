class Node:
    def __init__(self, key, color, left=None, right=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right


class LLRBTree:
    RED = True
    BLACK = False

    def __init__(self):
        self.root = None

    def is_red(self, node):
        if node is None:
            return False
        return node.color == self.RED

    def rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        right_child.color = node.color
        node.color = self.RED
        return right_child

    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        left_child.color = node.color
        node.color = self.RED
        return left_child

    def flip_colors(self, node):
        node.color = self.RED
        node.left.color = self.BLACK
        node.right.color = self.BLACK

    def insert(self, root, key):
        if root is None:
            return Node(key, self.RED)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)

        if self.is_red(root.right) and not self.is_red(root.left):
            root = self.rotate_left(root)
        if self.is_red(root.left) and self.is_red(root.left.left):
            root = self.rotate_right(root)
        if self.is_red(root.left) and self.is_red(root.right):
            self.flip_colors(root)

        return root

    def insert_key(self, key):
        self.root = self.insert(self.root, key)
        self.root.color = self.BLACK

    def inorder_traversal(self, node, result):
        if node:
            result = self.inorder_traversal(node.left, result)
            result.append(node.key)
            result = self.inorder_traversal(node.right, result)
        return result

    def display(self):
        if self.root is None:
            print("Tree is empty.")
            return

        def print_tree(node, indent, last):
            if node is not None:
                print(indent, end="")
                if last:
                    print("R----", end="")
                    indent += "     "
                else:
                    print("L----", end="")
                    indent += "|    "

                color = "RED" if node.color == "red" else "BLACK"
                print(f"({node.key}, {color})")
                print_tree(node.left, indent, False)
                print_tree(node.right, indent, True)

        print_tree(self.root, "", True)


# Example usage:
llrb_tree = LLRBTree()
keys = [10, 20, 30, 40, 50, 25, 5, 4, 3, 2, 1]

for key in keys:
    llrb_tree.insert_key(key)

llrb_tree.display()



