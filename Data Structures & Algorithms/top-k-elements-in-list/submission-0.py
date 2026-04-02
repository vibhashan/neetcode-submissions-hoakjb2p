class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 0
        
        hash_map = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))

        result = []
        for key, value in hash_map.items():
            if(k == 0):
                break
            else:
                result.append(key)
                k -= 1

        return result