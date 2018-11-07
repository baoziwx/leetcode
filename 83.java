/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return null;
        } else if (head.next == null) {
            return head;
        } else {
            head = deleteOne(head);
            ListNode curr = head;
            while (true) {
                curr.next = deleteOne(curr.next);
                if (curr.next == null) {
                    break;
                } else {
                    curr = curr.next;
                }
            }
            return head;
        }
    }
    public ListNode deleteOne (ListNode n) {
        if (n == null) {
            return null;
        } else if (n.next == null) {
            return n;
        } else if (n.val == n.next.val) {
            return deleteOne(n.next);
        } else {
            return n;
        }
    }
}