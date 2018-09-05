#Answer to Day 22: Binary Search Trees

    def getHeight(self,root):
        if root == None:
            return -1
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
#The above code recursively calls itself until it finds the last leaf node.