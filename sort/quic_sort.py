def qsort_rec(lst,l,r):
	if l>=r:
		return
	i=l
	j=r
	pivot=lst[i]
	while i<j:
		while i<j and lst[j]>=pivot:
			j-=1
		if i<j:
			lst[i]=lst[j]				
			i+=1						
		while i<j and lst[i]<=pivot:
			i+=1
		if i<j:
			lst[j]=lst[i]
			j-=1
	lst[i]=pivot
	qsort_rec(lst,l,i-1)		
	qsort_rec(lst,i+1,r)
	
list_test=[2,4,45,76,99,3,8,7]

qsort_rec(list_test,0,len(list_test)-1)
print(list_test)



