class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int ans = 0,x=0,y=0;
        for(auto &i: bank){
            for(auto &j: i){
                if(j=='1')x++;
            }
            if(x){
                ans += (x*y);
                y = x;
                x = 0;
            }
        }
        return ans;
    }
};