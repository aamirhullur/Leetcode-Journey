class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # hmap = {}
        # res = []
        # cnt = 0
        # for i in queries:
        #     if i[0] in hmap:
        #         hmap[i[0]] = i[1]
        #         cnt-=1
        #     else:
        #         hmap[i[0]] = i[1]
        #     cnt+=1
        #     # res.append(len(set(hmap.values())))
        #     res.append(cnt)
        # return res

        n = len(queries)
        result = []
        color_map = {}
        ball_map = {}

        # Iterate through queries
        for i in range(n):
            # Extract ball label and color from query
            ball, color = queries[i]

            # Check if ball is already colored
            if ball in ball_map:
                # Decrement count of the previous color on the ball
                prev_color = ball_map[ball]
                color_map[prev_color] -= 1

                # If there are no balls with previous color left, remove color from color map
                if color_map[prev_color] == 0:
                    del color_map[prev_color]

            # Set color of ball to the new color
            ball_map[ball] = color

            # Increment the count of the new color
            color_map[color] = color_map.get(color, 0) + 1

            result.append(len(color_map))

        return result
