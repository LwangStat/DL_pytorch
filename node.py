class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data <= self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            elif data > self.data:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

    def traverse(self, root):
        res = []
        if root.left:
            res = res + self.traverse(root.left)
        res.append(root.data)
        if root.right:
            res = res + self.traverse(root.right)
        return res

if __name__ == '__main__':
    n = Node(5)
    n.insert(7)
    n.insert(6)
    n.insert(3)
    print(n.traverse(n))