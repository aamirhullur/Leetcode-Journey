class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        # 1 : (2,4)
        # 2 : (1,3)
        # 3 : (0,2), (2,4)
        # 4 : (0,1), (1,3), (2,4)
        # 5 :        (0,2), (1,3), (2,4)
        # 6 :        (0,1), (0,2), (1,3), (2,4), (2,4)
                 
              
        # 1 : (1,3)
        # 2 : (0,2), (1,3)
        # 3 : (0,1), (0,2), (1,3), (1,3)
        # 4 :        , (0,1), (0,2), (0,2), (1,3), (1,3), (1,3)


        know, share = deque([(1,1)]), deque([])
        know_cnt, share_cnt = 1, 0
        for i in range(2,n+1):
            if know and know[0][0] == i - delay:
                know_cnt -= know[0][1]
                share_cnt += know[0][1]
                share.append(know[0])
                know.popleft()
            if share and share[0][0] == i - forget:
                share_cnt -= share[0][1]
                share.popleft()
            if share:
                know_cnt += share_cnt
                know.append((i,share_cnt))
        
        return (know_cnt + share_cnt) % (10**9+7)