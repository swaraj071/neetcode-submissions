import copy

class Twitter:

    def __init__(self):
        self.followBoard = defaultdict(list)
        self.userTweets = defaultdict(list)
        self.timer = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId not in self.followBoard.keys():
            self.followBoard[userId] = []

        tweet = (-self.timer, tweetId)
        self.timer += 1
        
        self.userTweets[userId].append(tweet)

        return
        

    def getNewsFeed(self, userId: int) -> List[int]:

        newsFeed = []

        for user in self.userTweets.keys():
            if user == userId or user in self.followBoard[userId]:
                for tweet in self.userTweets[user]:
                    newsFeed.append(tweet)

        heapq.heapify(newsFeed)

        finalFeed = []
        counter = 0

        while counter < 10 and len(newsFeed) > 0:
            tweet = heapq.heappop(newsFeed)
            finalFeed.append(tweet[1])
            counter += 1

        return finalFeed

        

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId == followeeId:
            return


        if followeeId not in self.followBoard[followerId]:
            self.followBoard[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.followBoard.keys():
            return

        if followeeId in self.followBoard[followerId]:
            self.followBoard[followerId].remove(followeeId)

        return

        
        
