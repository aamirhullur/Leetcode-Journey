class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        free_rooms = [i for i in range(n)] # (room_idx)
        heapq.heapify(free_rooms)

        used_room = [] # (end_time, room_idx)

        cnt = [0] * n  # [0,0,0]

        for start,end in meetings:

            duration = end - start

            while used_room and used_room[0][0] <= start:
                end_time,idx = heapq.heappop(used_room)
                heapq.heappush(free_rooms, idx)

            if free_rooms:
                idx = heapq.heappop(free_rooms)
            else:
                end_time, idx = heapq.heappop(used_room)
                end = end_time + duration

            heapq.heappush(used_room,(end,idx))
            cnt[idx] += 1
        print(cnt)
        res = (float('-inf'),float('inf'))
        for i in range(len(cnt)):
            if cnt[i] > res[0]:
                res = (cnt[i],i)
        
        return res[1]
