class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(root):
            if root is not None:
                inorder(root.left)
                result.append(root.val)
                inorder(root.right)
        result = []
        inorder(root1)
        inorder(root2)
        return sorted(result) 