class Solution {
public:
    bool isPalindrome(int x) {
        int y=x;
        if(x<0)
            return false;
            
        long int temp=0;
        while(y)
        {
            temp=temp*10+y%10;
            y/=10;
        }
        if(temp==x)
            return true;
        else
            return false;
    }
};
