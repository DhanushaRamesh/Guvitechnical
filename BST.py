class Node: 
    def __init__(self,data): 
        self.left = None
        self.right = None
        self.data = data
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def disp(self):
        if self.left:
            self.left.disp()
        print( self.data),
        if self.right:
            self.right.disp()
def getHeight(root):
    if root == None:
        return 0
    lh = getHeight(root.left)
    rh = getHeight(root.right)
    if lh>rh:
        return lh+1
    else:
        return rh+1

r=Node(50)
r.insert(30) 
r.insert(20) 
r.insert(40) 
r.insert(70)
r.insert(60) 
r.insert(80)
r.disp()
print("height:",getHeight(r))
