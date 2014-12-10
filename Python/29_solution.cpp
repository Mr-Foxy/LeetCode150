class Solution {
public:
    int maxProfit(vector<int> &prices) {
        // null check
        int len = prices.size();
        if (len==0) return 0;

        vector<int> historyProfit;
        vector<int> futureProfit;
        historyProfit.assign(len,0);
        futureProfit.assign(len,0);
        int valley = prices[0];
        int peak = prices[len-1];
        int maxProfit = 0;

        // forward, calculate max profit until this time
        for (int i = 0; i<len; ++i)
        {
            valley = min(valley,prices[i]);
            if(i>0)
            {
                historyProfit[i]=max(historyProfit[i-1],prices[i]-valley);
            }
        }

        // backward, calculate max profit from now, and the sum with history
        for (int i = len-1; i>=0; --i)
        {
            peak = max(peak, prices[i]);
            if (i<len-1)
            {
                futureProfit[i]=max(futureProfit[i+1],peak-prices[i]);
            }
            maxProfit = max(maxProfit,historyProfit[i]+futureProfit[i]);
        }
        return maxProfit;
    }
};
