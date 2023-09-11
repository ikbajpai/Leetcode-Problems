class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        // int sum=0;
        // int n = nums.size()-1;
        // for(int i=0;i<nums.size();i++){
        //     sum+=nums[i];
        // }
        // return sum-(n*(n+1)/2);

        sort(nums.begin(),nums.end());
        for (int i=0; i<nums.size()-1;i++){
            if(nums[i]==nums[i+1]) return nums[i];
        }
        return -1;
    }
};