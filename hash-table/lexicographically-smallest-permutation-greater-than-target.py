class Solution:
    def lexGreaterPermutation(self, s, target):
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - 97] += 1

        for i in range(len(target)):
            x = ord(target[i]) - 97

            if cnt[x] == 0:
                break

            cnt[x] -= 1

            if i == len(target) - 1:
                for j in range(i, -1, -1):
                    y = ord(target[j]) - 97
                    cnt[y] += 1

                    for c in range(y + 1, 26):
                        if cnt[c] > 0:
                            cnt[c] -= 1
                            suffix = ''.join(
                                chr(k + 97) * cnt[k] for k in range(26)
                            )
                            return target[:j] + chr(c + 97) + suffix
                return ""

        # target prefix cannot be matched, so increase the first
        # position that cannot be matched.
        for c in range(x + 1, 26):
            if cnt[c] > 0:
                cnt[c] -= 1
                suffix = ''.join(
                    chr(k + 97) * cnt[k] for k in range(26)
                )
                return target[:i] + chr(c + 97) + suffix

        # Backtrack if no direct increase is possible.
        for j in range(i - 1, -1, -1):
            y = ord(target[j]) - 97
            cnt[y] += 1

            for c in range(y + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1
                    suffix = ''.join(
                        chr(k + 97) * cnt[k] for k in range(26)
                    )
                    return target[:j] + chr(c + 97) + suffix

        return ""