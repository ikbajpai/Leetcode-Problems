class Solution {
public:
    bool isGood(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int sum=0;
        int n=nums.size();
        if(n>3 && nums[n-1] != nums[n-2]) return false;

        for(int i=0; i<n;i++){
            sum+=nums[i];
        }
        if(sum == n*(n+1)/2 - 1) return true;
        return false;
        

    }
};