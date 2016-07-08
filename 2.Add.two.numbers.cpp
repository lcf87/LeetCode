/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/*
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

 */ 

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    	struct ListNode *result = (struct ListNode *) malloc (sizeof(struct ListNode));
    	struct ListNode *curr   = result;
		int carry = 0;
		int sum = 0;

		while (l1 || l2) {
			// continue if l1 or l2 still has something left
			
			if (!l1) {
				// l1 no digit left, continue with l2
				sum = l2->val + carry;
				l2 = l2->next;
			} else if (!l2) {
				// l2 no digit left, continue with l1
				sum = l1->val + carry;
				l1 = l1->next;
			} else {
				// both are available
				sum = l1->val + l2->val + carry;
				l1 = l1->next;
				l2 = l2->next;
			}

			carry = (sum > 9) ? 1 : 0; 

			curr->val = sum % 10;

			if ((!l1) && (!l2) && (!carry)) {
				break;
			}

			curr->next = (struct ListNode *) malloc (sizeof(struct ListNode));
			curr = curr->next;
		}

		if (carry) {
			curr->val = 1;
		}	
		return result;
}
