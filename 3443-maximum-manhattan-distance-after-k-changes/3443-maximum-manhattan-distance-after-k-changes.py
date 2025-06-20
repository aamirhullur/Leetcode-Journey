class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        def flip(direction_pair: str) -> int:
            pos = 0             # net steps toward the target direction
            opposite_count = 0  # counts moves opposing the target
            best = 0
            for c in s:
                if c in direction_pair:
                    pos += 1
                else:
                    pos -= 1
                    opposite_count += 1
                # We can flip up to k opposing moves on the fly
                best = max(best, pos + 2 * min(k, opposite_count))
            return best
        
        return max(
            flip("NE"), flip("NW"),
            flip("SE"), flip("SW")
        )