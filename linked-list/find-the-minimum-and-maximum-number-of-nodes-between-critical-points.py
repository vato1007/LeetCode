class Solution:
    def nodesBetweenCriticalPoints(self, head):
        first = -1
        prev = -1
        min_dist = float('inf')

        pos = 1
        curr = head

        while curr and curr.next and curr.next.next:
            a = curr.val
            b = curr.next.val
            c = curr.next.next.val

            # Check whether b is a critical point
            if (b > a and b > c) or (b < a and b < c):
                if first == -1:
                    # First critical point
                    first = pos
                else:
                    # Distance from previous critical point
                    min_dist = min(min_dist, pos - prev)

                prev = pos

            curr = curr.next
            pos += 1

        # Fewer than two critical points
        if first == -1 or first == prev:
            return [-1, -1]

        # Maximum distance is between first and last
        max_dist = prev - first

        return [min_dist, max_dist]