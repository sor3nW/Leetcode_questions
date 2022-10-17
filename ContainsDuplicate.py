def containsDuplicate(nums):
	visit = set()
	for i in nums:
		if i in visit:
			return True
		else:
			visit.add(i)
	return False
#create a set 
#sets cannot contain duplicates
#for each number in nums check if the number has already been seen, and if it has then it is a duplicate so return True
#if there are no duplicates then return False 
#this is run in O(n) time while n is the length of array nums because the program has to run through the entire array 
