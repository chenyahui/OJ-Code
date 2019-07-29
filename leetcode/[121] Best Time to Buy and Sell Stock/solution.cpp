class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int len = prices.size();
        if(len < 2){
            return 0;
        }

        int result = 0;
        int max_num = prices.back();
        
        for(int i = len - 2; i >= 0; i--){
            result = std::max(max_num - prices[i], result);
            max_num = std::max(prices[i], max_num);
        }

        return result;
    }
};