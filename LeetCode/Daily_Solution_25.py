# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.seen=set()
        self.DFS(0,root)

    def find(self, target: int) -> bool:
        return target in self.seen
    
    def DFS(self, curr_val, currnode):
        if not currnode:
            return
        self.seen.add(curr_val)
        self.DFS(curr_val*2+1,currnode.left)
        self.DFS(curr_val*2+2,currnode.right)
        
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
