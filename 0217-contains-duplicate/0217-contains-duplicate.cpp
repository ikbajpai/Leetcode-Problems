class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        int sum=0;
        int n=nums.size();
        // if(nums.size()==1 && nums[0] == 0) return false;
        sort(nums.begin(),nums.end());
        for(int i=1; i<n; i=i+1){
            if(nums[i-1]==nums[i]) return true;
        }
        return false;
        
    }
};