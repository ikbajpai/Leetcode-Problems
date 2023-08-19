class Solution {
    public int[] countPoints(int[][] points, int[][] queries) {
        int n = queries.length;
        int[] res = new int[n];

        for (int i = 0; i < n; i++)
            res[i] = getAns(points, queries, i);
        return res;
    }

    public int getAns(int[][] points, int[][] queries, int i){
            int count = 0, centerX = queries[i][0], centerY = queries[i][1], radius = queries[i][2];

            for (int j = 0; j < points.length; j++) {
                int pointX = points[j][0], pointY = points[j][1];
                if ((pointX - centerX) * (pointX - centerX) + (pointY - centerY) * (pointY - centerY) <= radius * radius) count++;
            }
            return count;
    }
}