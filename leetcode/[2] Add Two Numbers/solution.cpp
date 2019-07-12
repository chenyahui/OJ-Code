/*
 * https://leetcode.com/problems/add-two-numbers/
 * 
 * @lc app=leetcode id=2 lang=cpp
 *
 * [2] Add Two Numbers
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* result = nullptr;
        ListNode* header = nullptr;

        bool has_rest = false;
        while(l1 || l2){
            int bit = has_rest?1:0;
            if(l1 != nullptr){
                 bit += l1->val;
                 l1 = l1->next;
            }

            if(l2 != nullptr){
                bit += l2->val;
                l2 = l2->next;
            }

            has_rest = bit >= 10;
            bit %= 10;

            auto node = new ListNode(bit);
            if(result){
                result->next = node;
                result = result->next;
            }else{
                result = node;
                header = node;
            }
        }

        if(has_rest){
            result->next = new ListNode(1);
        }

        return header;
    }
};