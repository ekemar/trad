#encoding: utf-8
import random
class TreeNode:
    def __init__(self, item, le=None, ri=None):
        self.item = item
        self.left = le
        self.right = ri
        self.parentFromLeft = None
        self.parentFromRight = None
        
    def height(self):
        if self.left == None and not self.right:
            return 1
            
        if self.right == None:
            return self.left.height() + 1
            
        if self.left == None:
            return self.right.height() + 1
            
        return max(self.left.height(), self.right.height()) + 1
    
    #def __str__(self):
        #return "<TreeNode with item=%s>" % self.item
        #return "<%s, l=%s, r=%s>" % (self.item, self.left, self.right)
        #return "%s\n <%s,%s>" % (self.item, self.left, self.right)
        
    def __str(self):
        return self.__repr() + "HEJ"

class Bintree:
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None
        
    def put(self, x):
        if self.root == None:
            self.root = TreeNode(x)
            return
        p = self.root
        
        while True:
            if x < p.item:
                if p.left == None:
                    p.left = TreeNode(x)
                    p.left.parentFromLeft = p
                    return
                else:
                    p = p.left
            elif x > p.item:
                if p.right == None:
                    p.right = TreeNode(x)
                    p.right.parentFromRight = p
                    return
                else:
                    p = p.right
            else:
                return
    
    def _deletenode(self, n):
        #print("in _deletenode, trying to delete node %s" % n)
        
        if n.right is None and n.left is None:
            print("inga barn finns")
            if n.parentFromLeft:
                n.parentFromLeft.left = None
            elif n.parentFromRight:
                n.parentFromRight.right = None
            n = None
        elif n.right is None:
            print("höger finns inte")
            if n.parentFromRight:
                n.parentFromRight.right = n.left
            elif n.parentFromLeft:
                n.parentFromLeft.left = n.left
            n = n.left
        elif n.left is None:
            print("vänster finns inte")
            if n.parentFromRight:
                n.parentFromRight.right = n.right
            elif n.parentFromLeft:
                n.parentFromLeft.left = n.right
            n = n.right
        else: #both left and right node exists: n.left and n.right isn't None
            goRight = random.choice([True, False])
            if goRight:
                print("Vi går åt höger")
                target = n.right
                while target.left:
                    target = target.left
                    
            else:
                print("Vi går åt vänster")
                target = n.left
                while target.right:
                    target = target.right
                
            n.item = target.item
            self._deletenode(target)
        #print("after deletion: %s" % n)
        return n
            
    def deletevalue(self, x):
        n = self.exists(x)
        if n:
            ret = self._deletenode(n)
        return ret
        
    def exists(self, x):
        """Returns the node p where p.item == x
        Returns None if there is no such p.item"""
        p = self.root
        
        while p != None:
            if x == p.item:
                return p
            elif x < p.item:
                p = p.left
            else:
                p = p.right
        
        return None
            
    def isempty(self):
        if self.root == None:
            return True
        else:
            return False
    
    def height(self):
        if self.root == None:
            return 0
        else:
            return self.root.height()
    
    def printtree(self):
        def inorder(p):
            if p ==  None:
                return []
            else:
                return inorder(p.left) + [p.item] + inorder(p.right)
                
        print(", ".join(map(str, inorder(self.root))))
        
    def printtreewidthfirst(self):
        s = [self.root]
        items = []
        while s:
            n = s.pop(0)
            items.append(n.item)
            
            if n.left:
                s.append(n.left)
            if n.right:
                s.append(n.right)
        print("width first: ", ", ".join(map(str, items)))
