class Solution {
public:
    int funcCircle(vector<int> point,vector<int> query){
        double S =(point[0] - query[0]) * (point[0] - query[0]) +
               (point[1] - query[1]) * (point[1] - query[1]) - query[2] * query[2];
        if(S<=0){
            return 1;
        }
        else{
            return 0;
        }
    }
public:
    vector<int> countPoints(vector<vector<int>>& points, vector<vector<int>>& queries) {
        vector<int>result;
        int count=0;
        for(int q=0; q<queries.size();q++){
            for(int p=0;p<points.size();p++){
                count+=funcCircle(points[p], queries[q]);
            }
            result.push_back(count);
            count=0;
        }
        return result;

        
    }
};