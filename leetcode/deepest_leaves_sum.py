from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
    
        q = deque([[root]])

        while q:
            level = q.popleft()
            next_level = []
            for node in level:
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)

            if len(next_level) == 0:
                return sum(node.val for node in level)
            q.append(next_level)
