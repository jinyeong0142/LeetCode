"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        ans = dfs(ans, root)
        return ans

def dfs(ans, node):
    if node != None:
        ans.append(node.val)
        for i in node.children:
            if i != None:
                ans = dfs(ans, i)
    return ans