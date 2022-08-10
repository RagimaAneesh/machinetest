def solution(nums,target):
    D = {}
    for i in range(len(nums)):
        D[nums[i]] = i
        for i in range(len(nums)):
            y = target-nums[i]
            if y in D:
                return [i,D[y]]
print(solution([2,7,11,15],9))