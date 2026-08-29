class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # (value, original index)
        pairs = sorted((value, i) for i, value in enumerate(nums))

        ans = nums[:]

        start = 0

        while start < n:
            end = start

            # Find the connected component
            while end + 1 < n and pairs[end + 1][0] - pairs[end][0] <= limit:
                end += 1

            # Values in this component
            values = [pairs[i][0] for i in range(start, end + 1)]

            # Original indices in this component
            indices = sorted(pairs[i][1] for i in range(start, end + 1))

            # Put smallest values at smallest indices
            for idx, value in zip(indices, values):
                ans[idx] = value

            start = end + 1

        return ans