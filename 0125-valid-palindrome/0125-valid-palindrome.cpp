class Solution {
public:
    bool isPalindrome(string s) {
        string str = "";
        if(1<= s.length() && s.length() <= 200000){
            for (char &i : s){
                if (isalnum(i)){
                    str += char(tolower(i));
                }
            }
            string rev = str;
            reverse(rev.begin(), rev.end());
            return str == rev;
        }
        else{
            return false;
        }
    }
};