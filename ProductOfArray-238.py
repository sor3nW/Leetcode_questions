#solution for leetcode question 238 Product of array except self
#difficulty - medium

out = [1] * len(nums) #creates a list of length of the input nums with bases at 1 so that we can do multiplication
prefix = 1 #we are using a prefix and postfix method to get the output we first get the prefix and multply the postfix by it
for i in range(len(nums)): #multiply the the output by the current prefix and then update the prefix while going down the list
    out[i] = prefix
    prefix *= nums[i]
    #prefix is created at this point so we can move onto making the postfix
postfix =1
for i in range(len(nums)-1,-1,-1): #we then go backwards through the list and do the same thing
    out[i] *= postfix
    postfix *= nums[i]
return out

#this solution is done in O(n) time and O(1) space complexity
