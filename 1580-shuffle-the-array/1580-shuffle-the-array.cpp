class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> v;
        for(int x=0; x<n; x++){
            v.push_back(nums[x]);
            v.push_back(nums[n+x]);
        }
        return v;
    }
};