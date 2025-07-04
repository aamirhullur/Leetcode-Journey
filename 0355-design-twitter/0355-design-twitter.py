class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        # self.tweets = []
        self.following = defaultdict(set)
        self.t = -1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.t,tweetId))
        # self.tweets.append([self.t,tweetId,userId])
        self.t-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        user = self.following[userId].copy()
        user.add(userId)

        # heap = []
        # for uid in user:
        #     if uid in self.tweets:
        #         for t,tweetId in self.tweets[uid][-10:]:
        #             print(t)
        #             heapq.heappush(heap,(t,tweetId))
        #             if len(heap) > 10:
        #                 heapq.heappop(heap)
        # print(heap)

        tweets = []
        for uid in user:
            tweets += self.tweets[uid][-10:]

        top10 = heapq.nsmallest(10, tweets)
        res = [tweetId for t, tweetId in sorted(top10)]
        # res = []


        # follow = self.following[userId]
        # follow.append(userId)
        # res = []
        # tweet = []
        # for t in self.tweets:
        #     if t[2] in follow:
        #         tweet.append(t)

        # heapq.heapify(tweet)

        # res = []
        # while len(res) != 10 and heap:
        #     time, tweetId = heapq.heappop(heap)
        #     res.append(tweetId)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # self.following[followerId].append(followeeId)
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # if followerId in self.following:
        #     idx = self.following[followerId].index(followeeId)
        #     self.following[followerId].pop(idx)

        # if followerId in self.following:
        self.following[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)