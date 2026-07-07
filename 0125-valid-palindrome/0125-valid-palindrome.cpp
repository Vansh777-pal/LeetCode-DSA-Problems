class Solution {
public:
    bool isPalindrome(string s) {
        string str = "";
        for (char &i : s){
            if (isalnum(i)){
                str += char(tolower(i));
            }
        }
        string rev = str;
        reverse(rev.begin(), rev.end());
        return str == rev;
    }
};