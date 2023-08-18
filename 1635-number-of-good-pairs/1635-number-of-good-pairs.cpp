class Solution {
public:
    int nc2(int n){
        return (n*(n-1)/2);}
public:
    int numIdenticalPairs(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int result=0;
        int count=1;
        for(int i=1; i<nums.size();i++){
            if(nums[i-1]==nums[i]){
                 count++;
            }

            else{
                result+=nc2(count);
                count=1;
            }
            
        }
        result += nc2(count);
        return result;

    }
};