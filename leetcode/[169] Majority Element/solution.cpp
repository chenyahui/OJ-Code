// 169. Majority Element
// https://leetcode.com/problems/majority-element/submissions/
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        auto len = nums.size();
        
        if(len <= 2) return nums[0];
        
        int max_num = nums[0];
        int cnt = 1;
        
        for(int i = 1; i < len; i++){
            if(cnt == 0){
                max_num = nums[i];
            }
            
            cnt += max_num == nums[i] ? 1 : -1;
        }
        
        return max_num;
    }
};