class Solution:
    def lexPalindromicPermutation(self, s, target):
        n = len(s)

        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Check if a palindromic permutation is possible
        odd = 0
        middle = ""

        for i in range(26):
            if count[i] % 2:
                odd += 1
                middle = chr(ord('a') + i)

        if odd > 1:
            return ""

        # Build the left half
        left = []

        for i in range(26):
            for _ in range(count[i] // 2):
                left.append(chr(ord('a') + i))

        def make_palindrome(left):
            left_str = ''.join(left)

            if n % 2:
                return left_str + middle + left_str[::-1]

            return left_str + left_str[::-1]

        # Smallest possible palindrome
        candidate = make_palindrome(left)

        if candidate > target:
            return candidate

        # Generate next permutations of the left half
        while True:
            i = len(left) - 2

            while i >= 0 and left[i] >= left[i + 1]:
                i -= 1

            if i < 0:
                return ""

            j = len(left) - 1

            while left[j] <= left[i]:
                j -= 1

            left[i], left[j] = left[j], left[i]

            left[i + 1:] = left[i + 1:][::-1]

            candidate = make_palindrome(left)

            if candidate > target:
                return candidate