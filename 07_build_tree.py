class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def creatTree(nodeList):
    if nodeList[0] == None:
        return None
    head = TreeNode(nodeList[0])
    Nodes = [head]
    j = 1
    for node in Nodes:
        if node != None:
            node.lchild = (TreeNode(nodeList[j]) if nodeList[j] != None else None)
            Nodes.append(node.lchild)
            j += 1
            if j == len(nodeList):
                return head
            node.rchild = (TreeNode(nodeList[j]) if nodeList[j] != None else None)
            j += 1
            Nodes.append(node.rchild)
            if j == len(nodeList):
                return head

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        res = []
        queue = [root]
        while queue:
            level_nums = len(queue)
            level_list = []
            for i in range(level_nums):
                cur = queue.pop()
                level_list.append(cur.val)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
            res.append(level_list)
        return res


if __name__ == '__main__':
    arr = [1,1,3,4]
    tree = creatTree(arr)
    solu = Solution()
    res = solu.levelOrder(tree)
