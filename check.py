def create_staircaseA(nums):
  while len(nums) != 0:
    step = 1
    subsets = []
    print(step)
    print(subsets)
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False

  return subsets
def create_staircaseB(nums):
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False
     
  return subsets

# Input
nums = [1, 2, 3, 4, 5, 6]

# First function call
print(create_staircaseA(nums))

# Second function call
print(create_staircaseB(nums))
