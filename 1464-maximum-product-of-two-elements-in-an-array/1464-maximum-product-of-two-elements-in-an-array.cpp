class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int maxi=INT_MIN;
        int smaxi=INT_MIN;
        int idx;
        for(int i=0;i<nums.size();i++){
            if(maxi<nums[i]) {
                maxi=nums[i];
                idx=i;
            }
        }
        for(int i=0;i<nums.size();i++){
            if(smaxi<nums[i]&&i!=idx) smaxi=nums[i];
        }
        return (maxi-1)*(smaxi-1);
    }
};