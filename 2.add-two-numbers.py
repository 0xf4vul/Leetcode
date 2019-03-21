#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (30.63%)
# Total Accepted:    796.5K
# Total Submissions: 2.6M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def list2num(node: ListNode) -> int:
            while node.next is not None:
                i = 0
                num = 0
                num += node.val * 10 ** i
                i += 1
            return num

def reverse(num):
    num = str(num)
    num = num[::-1]
    num = int(num)
    return num

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = list2num(l1)
        num2 = list2num(l2)
        sum = num1 + num2
        rev = reverse(num)
        rev = list(str(rev))
        return map(int, rev)


                
        

