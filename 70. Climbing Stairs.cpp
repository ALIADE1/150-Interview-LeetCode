class Solution {
public:
    int climbStairs(int n) {
        if (n == 1)
            return 1;
        if (n == 2)
            return 2;
        
        int li[n];
        li[0] = 1;
        li[1] = 2;
        
        for (int i = 2; i < n; i++) 
            li[i] = li[i-1] + li[i-2];
        
        return li[n-1];
    }
};
