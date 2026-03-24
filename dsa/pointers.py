def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    curr = 0
        
    for i in range(k):
        curr += nums[i]
        
    ans = curr/k
    for j in range(k, len(nums)):
        curr += nums[j] - nums[j-k]
        ans = max(ans, (curr/k))
        
    return ans
    
findMaxAverage([1,12,-5,-6,50,3], 4)
