class Solution {
public:
    int subtractProductAndSum(int n) {
        int sum=0;
        int prod=1;

        int temp = n;
        while(temp>0){
            sum+=temp%10;
            temp/=10;
        }

        while(n>0){
            prod*=n%10;
            n/=10;
        }
        return prod-sum;
        
    }
};