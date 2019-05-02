def quicksort(u,ini,fin):
  if ini<fin:
    pIndex = partition(u,ini,fin)
    quicksort(u,ini,pIndex-1)
    quicksort(u,pIndex+1,fin)
    
def partition(u,ini,fin):
  pivot = u[fin]
  i = ini-1
  for j in range(ini,fin):
    if u[j] < pivot:
      i += 1 
      u[i], u[j] = u[j], u[i]
  u[i+1], u[fin] = u[fin], u[i+1]
  return i + 1
  
def hanoi(n,start,tmp,final):
  if n > 0:
    hanoi(n-1,start,final,tmp)
    final.append(start.pop())
    hanoi(n-1,tmp,start,final)
    print(start,tmp,final)
    return True
  else:
    return True
