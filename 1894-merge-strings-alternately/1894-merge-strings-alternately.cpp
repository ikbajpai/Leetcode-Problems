class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int i=0;
        string str="";
        while(i<word1.length() || i< word2.length()){
            if(i<word1.length()){
                str+=word1[i];
            }
           if(i<word2.length()){
                str+=word2[i];
            }
            i++;
        }
        return str;
        
    }
};