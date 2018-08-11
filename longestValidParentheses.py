class Solution:
    def longestValidParentheses(self, s):
        """
        Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

        idea(WRONG!!):
        create a stack, read the char from the string one by one, if is '(', put in stack
        if is ')', pop element out

        increase the length by 2 each ')' is read, clear the counter only when stack is empty 
        or end of the string 

        idea(RIGHT):
        Use DP, construct an array l, let l[i] be the longest valid paretheses length thats end with i
        so when s[i] == '(', apparently l[i] = 0 coz no valid sequence ends with opening parenthese

        when s[i] == ')', it's value depends on the previous value.
        :type s: str
        :rtype: int
        """

        # if len(s) <= 1:
        #     return
        # stack = []
        # longest_length = 0
        # tmp_longest = 0
        # for c in s:
        #     if c == '(':
        #         stack.append(c)
        #     else:
        #         if not stack:
        #             # when stack is emtpy
        #             # compare the tmp_longest with the current longest
        #             # and clear the tmp_longest
        #             if tmp_longest > longest_length:
        #                 longest_length = tmp_longest
        #             tmp_longest = 0
        #         else:
        #             # when stack is not empty
        #             # pop out an '(' element
        #             # increase the tmp_longest by 2
        #             stack.pop()
        #             tmp_longest += 2
        # return max(longest_length, tmp_longest)
        if len(s) <= 1:
            return 0
        l = [None] * len(s)
        for index in range(len(s)):
            if s[index] == "(":
                l[index] = 0
            else:  # s[index] == ")"
                if index - 1 < 0:
                    l[index] = 0
                elif s[index - 1] == "(" and (index - 2 < 0
                                              or s[index - 2] == "("):
                    l[index] = 2
                elif s[index - 1] == "(" and index - 2 >= 0 and s[index -
                                                                  2] == ")":
                    l[index] = l[index - 2] + 2
                elif s[index - 1] == ")":
                    if index - l[index - 1] - 1 < 0 or s[index - l[index - 1] -
                                                         1] == ")":
                        l[index] = 0
                    elif index - l[index - 1] - 2 > 0:
                        l[index] = l[index - 1] + 2 + l[index - l[index - 1] -
                                                        2]
                    else:
                        l[index] = l[index - 1] + 2
        return max(l)