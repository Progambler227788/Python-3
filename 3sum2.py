def threeSum(nums):
        nums.sort()
        print(nums)
        data = []
        # to ensure that two elements left after first one
        for i in range( len(nums) - 2 ):
            left = i + 1
            right = len(nums) - 1
            if i>0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                target = nums[i] + nums[left] + nums[right]
            
                if target>0:
                    right -= 1
                    
                elif target < 0 :
                    left += 1
                    
                else:
                    data.append(  [ nums[i],nums[left],nums[right] ]  )
                    left+=1
                    while ( nums[left] == nums[left-1]  and left<right):
                        left +=1
                    
        return data
print(threeSum([3,2, -3, 0, 1,2,3,3,5,-3,0,0,0,2,34,5,4,3,3,3,3,3,3,2,2,2,2,2,2,2,1,1,1,1,1,1,0,0,0,0,3,3,3,2,4,3,4,34,35,34,34,3,3,3,3,3,3,3,3,3,3,12,12,12,12,12,12,12,12,12,12,19,129,-19,-19,-19,-19,-200,200,0,9,1,-1,90,0]))