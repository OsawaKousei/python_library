class Binary_tree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def insert_left(self, new_node):
        if self.left is None:
            self.left = Binary_tree(new_node)
        else:
            t = Binary_tree(new_node)
            t.left = self.left
            self.left = t

    def insert_right(self, new_node):
        if self.right is None:
            self.right = Binary_tree(new_node)
        else:
            t = Binary_tree(new_node)
            t.right = self.right
            self.right = t

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def set_root(self, obj):
        self.root = obj

    def get_root(self):
        return self.root

    def preorder(self):
        print(self.root)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.root)
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.root)


class Binary_tree_test:
    def setUp(self):
        self.t = Binary_tree("a")
        self.t.insert_left("b")
        self.t.insert_right("c")
        self.t.get_left().insert_right("d")
        self.t.get_right().insert_left("e")
        self.t.get_right().insert_right("f")

    def test(self):
        self.setUp()
        print("preorder")
        self.t.preorder()
        print("inorder")
        self.t.inorder()
        print("postorder")
        self.t.postorder()


def main():
    t = Binary_tree_test()
    t.test()


main()
