#include <vector>

class Solution {
public:
    int sum(vector<int>& nums) {
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }
        return totalSum;
    }

    int digitSum(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }

    int digitSum(vector<int>& nums) {
        int totalDigitSum = 0;
        for (int num : nums) {
            totalDigitSum += digitSum(num);
        }
        return totalDigitSum;
    }

    int differenceOfSum(vector<int>& nums) {
        int totalSum = sum(nums);
        int totalDigitSum = digitSum(nums);
        return abs(totalSum - totalDigitSum);
        
    }
};
