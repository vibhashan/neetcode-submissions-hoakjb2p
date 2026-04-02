class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = dict()

        for string in strs:
            sorted_string = "".join(sorted(string))

            if sorted_string in hash_map:
                hash_map[sorted_string].append(string)
            else:
                hash_map[sorted_string] = [string]

        result = []

        for key, value in hash_map.items():
            result.append(value)

        return result
        