class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l,r = 0, len(people)-1
        cnt = 0
        people.sort()

        while people[r] == limit and r > l:
                r-=1
                cnt+=1
        print(people)
        while l <= r:
            if l==r:
                cnt+=1
                break
            if people[l] + people[r] <= limit:
                l+=1
            r-=1
            cnt+=1
            print([people[l],people[r],cnt])


        return cnt
