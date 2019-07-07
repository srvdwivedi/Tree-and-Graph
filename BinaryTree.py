class BinaryTree():
    
    def __init__ (self,root):
        self.root = root
        self.rightChild = None
        self.leftChild = None
        
    def LeftInsert(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            t = BinaryTree(newNode)
            
    def RightInsert(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            t = BinaryTree(newNode)
            
    def setroot(self,ob):
        self.root = ob
    
    def getRight(self):
        return self.rightChild
    
    def getLeft(self):
        return self.leftChild
    
    def getRootVal(self):
        return self.root

            


# In[3]:


Bt = BinaryTree("a")


# In[5]:


Bt.getRootVal()


# In[7]:


Bt.RightInsert("B")
Bt.LeftInsert("C")


# In[10]:


Bt.getRight().getRootVal()

