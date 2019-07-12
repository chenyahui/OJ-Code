/*
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 * 
 * @lc app=leetcode id=3 lang=cpp
 *
 * [3] Longest Substring Without Repeating Characters
 */
class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        size_t len = s.size();
        if (len <= 1)
        {
            return len;
        }

        size_t start_index = 0;

        size_t result = 1;

        for (size_t i = 1; i < len; i++)
        {
            if (s[i] == s[i - 1])
            {
                start_index = i;
            }
            else
            {
                for (size_t j = start_index; j <= i - 1; j++)
                {
                    if (s[i] == s[j])
                    {
                        start_index = j + 1;
                        break;
                    }
                }
            }

            result = std::max(result, i - start_index + 1);
        }

        return result;
    }
};
