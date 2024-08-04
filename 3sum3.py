def threeSum(nums):
        maping = {}
        nums = sorted(nums)
        data = set()
        for i in range( len(nums) ):
            for j in range ( i+1, len(nums) ):
                target = - (nums[i] + nums[j])

                if target in maping and i!=j and i!= maping[target] and j!= maping[target]:     
                    trip =  [ nums[i] , target , nums[j] ] 
                    trip = tuple(sorted([nums[i], target, nums[j]]))  
                    if nums[i] + target + nums[j] == 0:
                       data.add( trip  )
                maping [ nums[j]  ] = j # key -> array value, value -> array index
        return [list(trip) for trip in data]
    
print(threeSum([3,2, -3, 0, 1,2,3,3,5,-3,0,0,0,2,34,5,4,3,3,3,3,3,3,2,2,2,2,2,2,2,1,1,1,1,1,1,0,0,0,0,3,3,3,2,4,3,4,34,35,34,34,3,3,3,3,3,3,3,3,3,3,12,12,12,12,12,12,12,12,12,12,19,129,-19,-19,-19,-19,-200,200,0,9,1,-1,90,0]))