class stack:
   def __init__(self):
      self.storage=[]
      self.count=0

   def empty(self):
      if (self.count==0):
         return True
      else:
         return False

   def store(self,x):
      self.storage = self.storage + [x]
      self.count = self.count + 1
      return True

   def retrieve(self):
      if (self.count==0):
         return [False,0]
      else:
         self.count = self.count - 1
         rval = self.storage[-1]
         self.storage = self.storage[0:-1]
         return [True,rval]

class queue:
    def __init__(self):
        self.storage=[]
        self.cnt = 0

    def empty(self):
       if self.cnt==0:
          return True
       else:
          return False

    def store(self,value):
        self.storage=self.storage+[value]
        self.cnt = self.cnt + 1
        return self.cnt

    def retrieve(self):
        if (self.cnt==0):
            return [False,0]
        else:
            r=self.storage[0]
            self.cnt=self.cnt-1
            self.storage=self.storage[1:]
            return [True,r]

class graph:
  def __init__(self):
    self.store = []
    
  def addVertex(self,n):
    if n == 0:
      return -1
    for i in range(0,n):
      self.store += [[]]
      n = len(self.store)
    return n 

  def addEdge(self, from_idx,to_idx, directed, weight):
    if weight == 0:
      return False
    if from_idx > len(self.store)-1:
      return False
    if to_idx > len(self.store)-1:
      return False
    if from_idx < 0:
      return False
    if to_idx < 0:
      return False
    if directed == True:
        self.store[from_idx] += [[to_idx,weight]]
        return True
    elif directed == False:
        self.store[from_idx] += [[to_idx,weight]]
        self.store[to_idx] += [[from_idx,weight]]
        return True
    else:
      return False
      
  def traverse(self,start,typeBreadth):
    n = 0
    if start > len(self.store):
      return []
    returnlist = []
    length = len(self.store)
    
    if typeBreadth == True: #breadth,queue
      C = queue()
    elif typeBreadth == False:
      C = stack()
    else:
      return []

    Discovered = [False]*length
    Processed = [False]*length
    
    if start == None:
      beg = 0
      end = len(self.store)

    else:
      beg = start
      end = start + 1
    

    for k in range(beg,end):
      if Discovered[k] == False:
        temp1 = k
        C.store(temp1)
        Discovered[k] = True
        if start == None:
          returnlist += [[]]

      val = C.retrieve()
      while val[0] == True:
        if Processed[val[1]] == False:
          if start == None:
            returnlist[len(returnlist)-1] += [val[1]]
          else:
            returnlist += [val[1]]
            Processed[val[1]] = True
        for h in self.store[val[1]]:
          if Discovered[h[0]] == False:
            temp2 = h[0]
            C.store(temp2)
            Discovered[h[0]] = True
        val = C.retrieve()
        
    return returnlist
    
  def connectivity(self,vx,vy):
    one = self.traverse(vx,False) 
    two = self.traverse(vy,False)
    
    returnlist = []
    
    print self.store
    print "one",one
    print "two",two
    
    for i in range(0,len(one)):
      if one[i] == vy:
        elone = True
        break
      else:
        elone = False

    for j in range(0,len(two)):
      if two[j] == vx:
        eltwo = True
        break
      else:
        eltwo = False
        
    return [elone,eltwo]

  def find_path(self, vx, vy):
    if vx == vy:
        return [vy]
    else:
        for new_vx in self.store[vx][0]:
                sub_path = self.find_path(new_vx, vy)
                if sub_path is not None:
                    return [vx] + sub_path


