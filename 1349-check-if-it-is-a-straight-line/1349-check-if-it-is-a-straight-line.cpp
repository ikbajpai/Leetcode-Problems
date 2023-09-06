class Solution {
public:
    bool lineFunc(vector<vector<int>>& coordinates){
    //    int m = /;
        int a=0;
        for(int i=2; i<coordinates.size();i++){
            a=(coordinates[i][1]-coordinates[0][1])*(coordinates[1][0]-coordinates[0][0]) - ((coordinates[1][1] - coordinates[0][1]))*(coordinates[i][0]-coordinates[0][0]);
            if(a){
                return false;
            }
        }
        return true;
    }
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        if(coordinates.size()<=2) return 1;

        return lineFunc(coordinates);


    }
};