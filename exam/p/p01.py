def p01(*nums):
    minnum=None
    # ↓程式區域↓
    minnum = nums[0]
    for i in range(1,len(nums)-1):
        if nums[i]< minnum:
            minnum = nums[i]
            nums.append(nums)
    # ↑程式區域↑
    return minnum
