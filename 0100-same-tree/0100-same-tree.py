# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(P, Q):
            if P == None and Q == None:
                return True
            if P == None or Q == None:
                return False
            return (
                P.val == Q.val
                and
                check(P.left, Q.left)
                and
                check(P.right, Q.right)
            )
        return check(p,q)