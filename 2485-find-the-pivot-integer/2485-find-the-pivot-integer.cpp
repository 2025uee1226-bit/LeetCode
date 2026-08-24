class Solution {
public:
    int pivotInteger(int n) {
        int i=1;
        int j=n;
        int sumi=1;
        int sumj=n;
        while(i<j){
            if(sumi<sumj){
                i++;
                sumi+=i;
            }
            else{
                j--;
                sumj+=j;
            }
        }
        if(sumi==sumj) return i;
        else return -1;
    }
};