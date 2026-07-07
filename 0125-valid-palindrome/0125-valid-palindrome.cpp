class Solution {
public:
    bool isPalindrome(string s) {
        // string str = "";
        // for (char &i : s){
        //     if (isalnum(i)){
        //         str += char(tolower(i));
        //     }
        // }
        // string rev = str;
        // reverse(rev.begin(), rev.end());
        // return str == rev;

        int i = 0;
        int j = s.size() - 1;
        while(i < j){
            while(i<j && !isalnum(s[i]) ){
                i ++;
            }
            while(i<j && !isalnum(s[j]) ){
                j --;
            }
            if(tolower(s[i]) != tolower(s[j])){
                return false;
            }
            else{
                i ++;
                j --;
            }
        }
        return true;
    }
};