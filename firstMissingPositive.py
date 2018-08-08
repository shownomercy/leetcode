class Solution:
    def firstMissingPositive(self, a_list):
        """Given an unsorted integer array, find the smallest missing positive integer.
        solution needs to be O(n) time complexity and constant extra space
        Input: [1,2,0]
        Output: 3

        Input: [3,4,-1,1]
        Output: 2


        Arguments:s
            a_list {[list]}
        """

        def segerate(a_list):
            j = 0
            for i in range(0, len(a_list)):
                if a_list[i] <= 0:
                    a_list[i], a_list[j] = a_list[j], a_list[i]
                    j += 1
            return j

        first_positive_index = segerate(a_list)

        def my_abs(value):
            if value <= 0:
                return -value
            return value

        all_positive_count = len(a_list) - first_positive_index

        for i in range(all_positive_count):
            if my_abs(a_list[first_positive_index +
                             i]) < all_positive_count + 1 and a_list[my_abs(
                                 a_list[first_positive_index +
                                        i]) - 1 + first_positive_index] > 0:

                a_list[my_abs(a_list[first_positive_index + i]) +
                       first_positive_index -
                       1] = -a_list[my_abs(a_list[first_positive_index + i]) +
                                    first_positive_index - 1]

        for i in range(first_positive_index, len(a_list)):
            if a_list[i] > 0:
                return i - first_positive_index + 1

        return len(a_list) - first_positive_index + 1


s = Solution()
#fmp = s.firstMissingPositive([-3, 5, -199, 1, 4, 5, 10]) # 2
#fmp = s.firstMissingPositive([-3, -5, -199, -1, -4, -5, 1, -10])  # 2
#fmp = s.firstMissingPositive([3, -5, -199, -1, -4, -5, 0, -10])  # 2
#fmp = s.firstMissingPositive([1, 1])  # 2
#fmp = s.firstMissingPositive([2, 2])  # 2
fmp = s.firstMissingPositive([1, 2, 0])  # 2
print(fmp)
