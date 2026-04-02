class Solution {
    public boolean hasDuplicate(int[] nums) {
        // Convert to a set
        // If nums.length == set.length, no duplicates, else duplicates exist
        Set<Integer> numsSet = new HashSet<>();
        for (int num : nums){
            numsSet.add(num);
        }

        return numsSet.size() != nums.length;
    }
}