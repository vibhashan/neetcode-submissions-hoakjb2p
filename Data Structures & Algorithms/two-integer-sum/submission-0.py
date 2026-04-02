class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()

        for i, num in enumerate(nums):
            target_num = target - num
            if target_num in hash_map:
                return [hash_map[target_num], i]
            else:
                hash_map[num] = i

        return []        
