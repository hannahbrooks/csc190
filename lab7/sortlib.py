def selection_sort(u):
	n = len(u)
	if n<=1:
		return False
	for i in range(n): 
	    min_idx = i 
	    for j in range(i+1, n): 
	        if u[min_idx] > u[j]: 
	            min_idx = j       
	    u[i], u[min_idx] = u[min_idx], u[i] 
	return True

def heapify(u):
	count = len(u)
	start = (count-1)/2
	while start >= 0:
		helper_siftDown(u,start,count-1)
		start = start - 1 
	return True

def helper_siftDown(u,start,end):
	root = start
	while root*2 + 1 <= end:
		child = 2*root + 1 
		swap = root
		if u[swap] > u[child]:
	  		swap = child
		if child + 1 <= end and u[swap] > u[child+1]:
	  		swap = child + 1 
		if swap == root:
	  		return True
		else:
	  		u[root], u[swap] = u[swap], u[root]
	  		root = swap
	return True

def reheapify(u,end):
	u[0] = u[end]
	u.pop(end)
	root = 0
	while root*2 + 1 <= end-1:
		child = 2*root + 1 
		swap = root
		if u[swap] > u[child]:
	  		swap = child
		if child + 1 <= end-1 and u[swap] > u[child+1]:
	 		 swap = child + 1 
		if swap == root:
	  		return True
		else:
			u[root], u[swap] = u[swap], u[root]
	  		root = swap
	return True

def heap_sort(u):
	temp = []
	end = len(u)-1
	heapify(u)

	for i in range(0,len(u)):
		temp += [u[0]]
		reheapify(u,end)
		end -= 1 
	for j in range(0,len(temp)):
		u += [temp[j]]
	return True

def merge_sort(u):
	if len(u) == 1:
		return True

	mid = len(u)//2

	a = u[:mid]
	b = u[mid:]

	merge_sort(a)
	merge_sort(b)

	i = 0
	j = 0
	k = 0
	  
	while i < len(a) and j < len(b): 
	    if a[i] < b[j]: 
	        u[k] = a[i] 
	        i+=1
	    else: 
	        u[k] = b[j] 
	        j+=1
	    k+=1
	  
	# Checking if any element was left 
	while i < len(a): 
	    u[k] = a[i] 
	    i+=1
	    k+=1
	  
	while j < len(b): 
	    u[k] = b[j] 
	    j+=1
	    k+=1

	return True
