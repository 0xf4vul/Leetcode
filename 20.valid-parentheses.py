#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (35.94%)
# Total Accepted:    536.7K
# Total Submissions: 1.5M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def top(self):
        return self.items[-1]
    def size(self):
        return len(self.items)

class Solution:
    def isValid(self, s: str) -> bool:
        if s == '':
            return True
        else:
            l = list(s)
            dic = {'(': ')', '[': ']', '{': '}'}
            stack = Stack()
            for p in l:
                if p in ['(', '[', '{']:
                    stack.push(p)
                else:
                    if (not stack.is_empty()) and (dic[stack.top()] == p):
                        stack.pop()
                    else:
                        return False
            return stack.is_empty()



