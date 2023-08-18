class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        vector<double> res;
        res.push_back(celsius+273.15);
        res.push_back(1.80*celsius + 32);
        return res;
        
    }
};