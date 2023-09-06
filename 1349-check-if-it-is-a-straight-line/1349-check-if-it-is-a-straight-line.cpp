class Solution {
public:
    // Helper function to check if a set of coordinates lies on the same line.
    bool lineFunc(vector<vector<int>>& coordinates) {
        int a = 0;
        for (int i = 2; i < coordinates.size(); i++) {
            a = (coordinates[i][1] - coordinates[0][1]) * (coordinates[1][0] - coordinates[0][0]) -
                ((coordinates[1][1] - coordinates[0][1])) * (coordinates[i][0] - coordinates[0][0]);
            if (a) {
                return false;
            }
        }
        return true;
    }

    // Main function to check if all coordinates form a straight line.
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        if (coordinates.size() <= 2) {
            return true; // If there are 2 or fewer coordinates, they always form a straight line.
        }

        return lineFunc(coordinates);
    }
};
