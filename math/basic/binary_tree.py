class Binary_tree:
    def __init__(self, root):
        self.root = root
        self.res = []
        self.left = None
        self.right = None
        self.top = None

    def set_top(self):
        if self.top is None:
            return self
        else:
            return self.top

    def insert_left(self, new_node):
        if self.left is None:
            self.left = Binary_tree(new_node)
            self.left.top = self.set_top()
        else:
            t = Binary_tree(new_node)
            t.top = self.set_top()
            t.left = self.left
            self.left = t

    def insert_right(self, new_node):
        if self.right is None:
            self.right = Binary_tree(new_node)
            self.right.top = self.set_top()
        else:
            t = Binary_tree(new_node)
            t.top = self.set_top()
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
        self.res = []
        if self.left:
            self.left.inorder()

        if self.top is None:
            self.res.append(self.root)
        else:
            self.top.res.append(self.root)

        if self.right:
            self.right.inorder()

        return self.res

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.root)

    def show(self, res):
        print("show")
        print(res)


class Binary_tree_test:
    def setUp(self):
        self.t = Binary_tree("a")
        self.t.insert_left("b")
        self.t.left.insert_left("c")
        self.t.left.insert_right("d")
        self.t.insert_right("e")
        self.t.right.insert_right("g")
        self.t.right.insert_left("f")
        self.t.right.right.insert_right("h")
        self.t.right.right.insert_left("i")

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
    t.t.show(t.t.inorder())


# main()

"""memo
＜クラスメソッドにおいて＞

def func(self):
    return self

def show(input):
    print(input) ←これはエラーになる(暗黙的にselfが渡されるため)

以下のようにするとエラーにならない
def show(self, input):
    print(input)

@staticmethod
def show(input):
    print(input)

self.top = self ←これは問題を起こす？

"""
