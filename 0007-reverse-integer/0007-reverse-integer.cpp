class Solution {
public:
    int reverse(int x) {
        int revNum = 0;
        while(x != 0) {
            int digit = x % 10;
            if (revNum > 214748364 || revNum < -214748364)
                return 0;
            revNum = (revNum * 10) + digit; 
            x = x/10;
        };
        return revNum;
    }
};