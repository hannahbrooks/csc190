from class_queue import*
from tree import*


class binary_tree:
   def __init__(self,x):
      self.store = [x,[],[]]

   def Print_DepthFirst(self):
      self.Print_DepthFirst_mid("   ")
      return True


   def Print_DepthFirst_mid(self,pre):
      print (pre+str(self.store[0]))
      for i in self.store[1]:
         i.Print_DepthFirst_mid(pre+"   ")
         return True

   def Get_Level_Order(self):
      x=queue()
      x.enqueue(self)
      accum=[]
      while True:
         rval=x.dequeue()
         if (rval[0]==False):
            break
         L = rval[1]
         if (rval[1]==[]):
            continue
         else:
            accum = accum + [L.store[0]]
            x.enqueue((L.store)[1])
            x.enqueue((L.store)[2])
      return accum

   def AddRight(self,BR):
      self.store[2] = BR

   def AddLeft(self,BL):
      self.store[1] = BL

   def ConvertToTree(self):
      lst = self.Get_Level_Order()
      new = tree(lst[0])
      for i in range(1, len(lst)):
         x = tree(lst[i])
         new.AddSuccessor(x)

      return [True, new]

