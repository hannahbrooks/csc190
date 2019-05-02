from class_queue import*
from binary_tree import*

class tree:
   def __init__(self,x):
      self.store = [x,[]]

   def AddSuccessor(self,x):
      self.store[1] = self.store[1] + [x]
      return True

   def Print_DepthFirst(self):
      self.Print_DepthFirst_mid("    ")
      return True


   def Print_DepthFirst_mid(self,pre):
      print (pre+str(self.store[0]))
      for i in self.store[1]:
         i.Print_DepthFirst_mid(pre+"   ")
      return True

   def Get_Level_Order(self):
      x=queue()
      x.enqueue(self.store)
      accum=[]
      while True:
         rval=x.dequeue()
         if (rval[0]==False):
            break
         else:
            q=rval[1]
            accum=accum+[q[0]]
            for element in q[1]:
               x.enqueue(element.store)
      return accum


   def ConvertToBinaryTree(self):
      lst = self.Get_Level_Order()
      new = binary_tree(self.store[0])
      temp = new
      for i in range(len(lst)):
         x = binary_tree(lst[i])
         temp.store[1] = [x]
         temp = x

      return new

