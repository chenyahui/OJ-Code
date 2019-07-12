/*
 * https://leetcode.com/problems/longest-palindromic-substring
 *  
 * @lc app=leetcode id=5 lang=cpp
 *
 * [5] Longest Palindromic Substring
 */
class Solution
{
public:
    string longestPalindrome(string s)
    {
        size_t len = s.size();
        if (len <= 1)
        {
            return s;
        }

        std::vector<std::vector<bool>> dp(len, std::vector<bool>(len, false));

        for (size_t i = 0; i < len; i++)
        {
            dp[i][i] = true;
        }

        size_t longest_start = 0;
        size_t max_len = 1;

        for (int i = len - 1; i >= 0; i--)
        {
            for (int j = i + 1; j < len; j++)
            {
                dp[i][j] = s[i] == s[j] && (j == i + 1 || dp[i + 1][j - 1]);
                
                size_t local_len = j - i + 1;
                if (dp[i][j] && local_len > max_len)
                {
                    longest_start = i;
                    max_len = local_len;
                }
            }
        }

        return s.substr(longest_start, max_len);
    }
};
