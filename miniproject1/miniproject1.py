def finder(nums):
    subsets = []
    curr = []

    def backtrack(start, target):
        if len(curr) == 5 and target == 0:
            subsets.append(curr[:])
            return
        if len(curr) > 5 or target < 0:
            return
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtrack(i + 1, target - nums[i])
            curr.pop()

    backtrack(0, 0)
    return subsets

 
num=[]
n=int(input("enter number of elements"))
for i in range(n):
    m=int(input(""))
    num.append(m)
sets=finder(num)
print(sets)