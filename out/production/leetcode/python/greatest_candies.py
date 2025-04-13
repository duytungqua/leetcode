
class Solution:
    def gratest_candies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]