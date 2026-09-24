# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        if root.val == subRoot.val:
            ans = self.confirmEquality(root, subRoot)
            if ans:
                return ans
        
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
    
    def confirmEquality(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        
        if root.val == subRoot.val:
            return self.confirmEquality(root.right, subRoot.right) and self.confirmEquality(root.left, subRoot.left)
        else:
            return False
