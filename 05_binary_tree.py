class Node():
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None

class binary_tree():
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root == None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        # 层次遍历或者广度遍历
        if self.root == None:
            print('None')
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item, end=' ')
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self, node):
        # 前序遍历
        if self.root == None:
            return
        if node is None:
            return
        print(node.item, end=' ')
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        # 中序遍历
        if self.root == None:
            return
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.item, end=' ')
        self.inorder(node.rchild)

    def postorder(self, node):
        # 后序遍历
        if self.root == None:
            return
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.item, end=' ')


if __name__ == '__main__':
    tree = binary_tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(' ')
    tree.preorder(tree.root)
    print(' ')
    tree.inorder(tree.root)
    print(' ')
    tree.postorder(tree.root)