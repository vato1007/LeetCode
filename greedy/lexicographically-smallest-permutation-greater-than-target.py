class Solution:
    def lexGreaterPermutation(self, s, target):
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - 97] += 1

        used = 0

        for i in range(len(target)):
            x = ord(target[i]) - 97

            if cnt[x] == 0:
                break

            cnt[x] -= 1
            used += 1
        else:
            used = len(target)

        for i in range(used - 1, -1, -1):
            x = ord(target[i]) - 97
            cnt[x] += 1

            for c in range(x + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1
                    suffix = ''.join(
                        chr(j + 97) * cnt[j] for j in range(26)
                    )
                    return target[:i] + chr(c + 97) + suffix

        return ""